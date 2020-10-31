import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dashboard.base import app
from database import User
from database import session
from dash.exceptions import PreventUpdate


fields = html.Div(
    [
        dbc.Input(id="user_name", placeholder="Type firstname", type="text"),
        dbc.Input(id="user_last_name", placeholder="Type lastname", type="text"),
        dbc.Input(id="user_id", placeholder="Type user_id", type="number"),
    ],
    style={"width": "300px"},
)
layout = html.Div(
    [
        fields,
        dbc.Button("Find", id="user_find", color="secondary", className="mr-1",n_clicks= 0),
        dbc.Button("Create", id="user_create", color="primary", className="mr-1", n_clicks =0),
        html.Div(id="user_result_1"),
        html.Div(id="user_result_2"),

    ]
)


@app.callback(
    Output("user_result_1", "children"),
    [Input("user_create", "n_clicks")],
    [
        State("user_name", "value"),
        State("user_last_name", "value"),
        State("user_id", "value"),
    ],
)
def create_user(n_click, first_name, last_name, user_id):
    if n_click > 0:
        user = User(first_name=first_name, last_name=last_name, user_id=user_id)
        session.add(user)
        session.commit()
        return f"name: {user.first_name} , id = {user.user_id}, id_ = {user.id} "
    raise PreventUpdate


@app.callback(
    Output("user_result_2", "children"),
    [Input("user_find", "n_clicks")],
    [
        State("user_id", "value"),
    ],
)
def find_user(n_click, user_id):
    if n_click > 0:
        user =  User.query.filter_by(user_id=9836).first()
        if user :
            return f"name: {user.first_name} , id = {user.user_id}, id_ = {user.id} "
        else:
            return "NO user."
    raise PreventUpdate
    