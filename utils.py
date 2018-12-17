from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.model_selection import KFold
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error # error metric
from math import sqrt

def rmse(model, y, x):
    return sqrt(mean_squared_error(y, model.predict(x)))

def cols2numeric(df):
    df.drop("Vin",1,inplace=True)
    df[["City","State","Make", "Model"]] = df[["City","State","Make", "Model"]].astype('category')
    cat_columns = df.select_dtypes(['category']).columns
    df[cat_columns] = df[cat_columns].apply(lambda x: x.cat.codes)
    return df

def preparing_data(csv_name="true_car_listings.csv",to_numeric=True,IQR=True):
    df = pd.read_csv(csv_name)
    if(to_numeric):
        df = cols2numeric(df)
    if(IQR):
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
        
    X = df[["Year","Mileage","City","State","Make","Model"]]
    y = df["Price"]
    
    return X,y

def cross_validation(model, X,y,n_splits=10,shuffle=False,random_state=None):
    kf = KFold(n_splits=n_splits) 
    kf.get_n_splits(X) # returns the number of splitting iterations in the cross-validator
    KFold(n_splits=n_splits, random_state=random_state, shuffle=shuffle)
    list_rmse_train = []
    list_rmse_test = []
    trained_model = []
    
    for train_index, test_index in kf.split(X):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]
        model.fit(X_train, y_train)
        list_rmse_train.append(rmse(model, y_train, X_train))
        list_rmse_test.append(rmse(model, y_test, X_test))
        trained_model.append(model)
    
    return list_rmse_train,list_rmse_test,trained_model

