import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.SOLAR],suppress_callback_exceptions = True)