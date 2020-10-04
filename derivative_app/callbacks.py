
# for app
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash
import plotly.graph_objects as go
from dash.dependencies import Output, Input, State
# writing to excel files
from dash.exceptions import PreventUpdate
from app import app
import numpy as np


def parabola(x): 
    return np.power(x,2)

def sine(x):
    return np.sin(x)

def cosine(x): 
    return np.cos(x)

def cubic(x): 
    return np.power(x,3)

def quartic(x): 
    return np.power(x,4)

def logistic(x): 
    return 1/(1+np.exp(-x))
    
def log_func(x):
    return np.log(x)

def derivative(f, start_x, dx): 
    x0 = start_x
    xnew = x0+dx
    y0 = f(x0-dx)
    ynew = f(x0+dx)
    ratio = (ynew-y0)/(2*(xnew-x0))
    return ratio




@app.callback([
                Output('x-slider', 'min'),
                Output('x-slider', 'max'),
                Output('func-plot','figure'),
                Output("derivative-plot", "figure")],
              [Input("functions", "value"),
               Input('x-slider', 'value'),
               Input('dx-slider', 'value')])
def update_func(dropdown_value, x, dx):
    x_range = np.arange(-100,100,0.01)
    func_type = {'parabola': parabola, 
                'cubic': cubic,
                'quartic':quartic, 
                'sine':sine,
                'log':log_func,
                'cosine': cosine,
                'logistic': logistic}
    
    y_range_dict = {'parabola': [-10000,10000], 
                'cubic': [-100,100],
                'quartic':[-100000,100000], 
                'sine':[-1,1],
                'log':[0,4],
                'cosine': [-1,1],
                'logistic': [-0.5,1.5]}
    
    x_range_dict = {'parabola': [-100,100], 
                'cubic': [-10,10],
                'quartic':[-100,100], 
                'sine':[-100,100],
                'log':[0,10],
                'cosine': [-100,100],
                'logistic': [-100,100]}

    x_range_der = {'parabola': [-100,100], 
                'cubic': [-100,100],
                'quartic':[-100,100], 
                'sine':[-100,100],
                'log':[0,10],
                'cosine': [-100,100],
                'logistic': [-100,100]}
    f = func_type[dropdown_value]
    func_name = dropdown_value

    slope = derivative(f, x, dx)
    trace1 = go.Scatter(
        x = x_range,
        y = f(x_range),
        mode="lines",
        name=func_name
    )
    intercept = f(x+dx) - (slope*(x+dx))
    df_dx = slope*x_range + intercept
 
    pt_x = [x-dx, x+dx]
    pt_y = [f(x-dx), f(x+dx)]
    trace2 = go.Scatter(
    x = x_range,
        y = df_dx,
        mode="lines",
        name="Derivative"
        )

    trace3 = go.Scatter(
    x= pt_x, 
    y= pt_y,
    mode="markers",
    name= "Intercepts",
    marker= dict(color="red"))
    data = [trace1, trace2, trace3]

    layout = go.Layout(yaxis=dict(range=y_range_dict[dropdown_value]),
                       xaxis=dict(range=x_range_dict[dropdown_value]))
    
    
    
    figure_func = go.Figure(data=data, layout=layout)

    trace_der = derivative(f,x_range,dx)
    trace_der_plot = go.Scatter(x=x_range,
                           y=trace_der,
                           mode="lines",
                           )
    trace_der_point = go.Scatter(x=[x],
                                y=[slope],
                                mode="markers",
                                marker=dict(color="red"))

    data2 = [trace_der_plot, trace_der_point]
    layout = go.Layout(xaxis=dict(range=x_range_der[dropdown_value]))

    derivative_fig = go.Figure(data=data2, layout=layout)
    x_min = x_range_dict[dropdown_value][0]
    x_max = x_range_dict[dropdown_value][1]
    return [ x_min, x_max, figure_func, derivative_fig]


@app.callback(Output("x-slider-output", "children"),
             [Input("x-slider", "value")])
def print_x_slider(value): 
    children = "x-axis value is {}".format(value)
    return children

@app.callback(Output("dx-slider-output", "children"),
             [Input("dx-slider", "value")])
def print_x_slider(value): 
    children = "dx-axis value is {}".format(value)
    return children