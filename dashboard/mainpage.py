from .base import app, html, dcc
from .navbar import navbar
from .pages import home
from .callbacks import render_page_content


app.layout = html.Div(children=[
    navbar,
    dcc.Location(id="url"),

    html.Div(id='root'),

])

