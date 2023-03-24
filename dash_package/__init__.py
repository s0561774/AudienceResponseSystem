# Initialize Flask app
from flask import Flask
import dash
import dash_bootstrap_components as dbc

# Create a server Flask.
server = Flask(__name__)

server.config['DEBUG'] = True

# Create a Plotly Dash dashboard.
app = dash.Dash(__name__, server=server, url_base_pathname='/dashApp/',
                             external_stylesheets=[dbc.themes.BOOTSTRAP, 'dashboard.css'])
app.config['suppress_callback_exceptions'] = True

#Import parts of our core Flask app
from dash_package import routes