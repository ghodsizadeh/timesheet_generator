import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from .navbar import navbar
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.SOLAR])



app.layout = html.Div(children=[
    navbar,
    html.H1(children='Hello Dash'),

    html.Div(id='root'),

])