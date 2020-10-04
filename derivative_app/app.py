import dash
from flask import Flask 





# server = Flask(__name__) # define flask app.server

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'])
app.config.suppress_callback_exceptions = True
server = app.server
