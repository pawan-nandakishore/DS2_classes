import os
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash
import plotly.graph_objects as go
from dash.dependencies import Output, Input

functions =[
            {'label': 'Parabola', 'value': 'parabola'},
            {'label': 'Cubic', 'value': 'cubic'},
            {'label': 'Quartic', 'value': 'quartic'},
            {'label': 'Sine', 'value': 'sine'},
            {'label': 'logistic', 'value': 'logistic'},
             {'label': 'Logrithmic', 'value': 'log'}   
        ]

# APP LAYOUT
layout1 = html.Div(children=[
html.H1("Derivative of a Function"),

html.H6("Choose a function"),
html.Div([
    dcc.Dropdown(
        id="functions",
        options=functions,
        value="parabola"
    )

]),

html.H6("Adjust the x value"), 
html.Div([

    dcc.Slider( id='x-slider',
        min=-100,
        max=100,
        step=1,
        value=10,
        tooltip={'placement': 'top', 'always_visible': True}
    ),
    html.Div(id='x-slider-output')
]),

html.H6("Adjust the dx value"), 
html.Div([

    dcc.Slider( id='dx-slider',
        min=0,
        max=5,
        step=0.1,
        value=1,
        tooltip={'placement': 'top', 'always_visible': True}
    ),
    html.Div(id='dx-slider-output')
]),


html.Div([
    html.Div([
            dcc.Graph(id="func-plot")
    ], className='six columns'), 

    html.Div([
            dcc.Graph(id="derivative-plot")
    ], className='six columns')
], className="row")

])