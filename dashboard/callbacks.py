from .base import app, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from .pages import home, user

@app.callback(Output("root", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/user":
        return user.layout

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("خطای ۴۰۴. چیزی پیدا نشد", className="text-danger"),
            html.Hr(),
            html.P(f"مسیر {pathname} پیدا نشد..."),
        ]
    )


