# Results represented graphically

Directory created to graphically represent the results we obtained in the experiments of this project.

The first three graphs were created from random samples
of data (50 elements) taken from each model, one of the lines
representing the true data and the other the predictions of the
model for the test set.

To create the last graph, where the errors of each model are compared, 
we use the cross validation technique by repeating the experiment 10 times, 
so we calculate the mean of the errors and the respective standard deviations.

### How to run
 * install the dependencies:
    ```sh 
    npm install
    ```
 * run the application:
    ```sh 
    npm start
    ```
