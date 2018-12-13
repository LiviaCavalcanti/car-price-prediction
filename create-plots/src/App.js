import React, { Component } from 'react';
import DecisionTreePlot from './components/DecisionTreePlot'
import GradientBoosting from './components/GradientBoosting'
import LinearRegression from './components/LinearRegression'
import ErrorsPlot from './components/ErrorsPlot' 
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <h1>Decision Tree</h1>
        <DecisionTreePlot></DecisionTreePlot>
        <h1>Gradient Boosting</h1>
        <GradientBoosting></GradientBoosting>
        <h1>Linear Regression</h1>
        <LinearRegression></LinearRegression>
        <h1>Errors Plot</h1>
        <ErrorsPlot></ErrorsPlot>
      </div>
    );
  }
}

export default App;
