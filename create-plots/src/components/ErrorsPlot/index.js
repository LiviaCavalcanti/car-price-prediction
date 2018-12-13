import React from 'react';
import Plot from 'react-plotly.js';

class App extends React.Component {
    render() {
        return (
            <div>
                <Plot
                    data={[
                        {
                            x: ['Decision Tree', 'Gradient Boosting', 'Linear Regression'],
                            y: [85.06, 7504.78, 7939.56],
                            name: 'Train',
                            error_y: {
                                type: 'data',
                                array: [7.65, 103.25, 68.18],
                                visible: true
                            },
                            type: 'bar',
                            marker: { color: '#37778f' },
                        },
                        {
                            x: ['Decision Tree', 'Gradient Boosting', 'Linear Regression'],
                            y: [9993.11, 8549.04, 8198.77],
                            name: 'Test',
                            error_y: {
                                type: 'data',
                                array: [1596.92, 747.80, 625.12],
                                visible: true
                            },
                            type: 'bar',
                            marker: { color: '#6a051c' },
                        }
                    ]}
                    layout={{ width: 1000, height: 500, title: 'Comparison of the mean of the errors in the different models' }}
                />



            </div>
        );
    }
}

export default App;