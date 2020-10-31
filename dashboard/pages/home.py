
import dash_bootstrap_components as dbc
import dash_html_components as html



card = dbc.Card(
    [
        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)

layout = html.Div(
    [
        dbc.Button("Generate TimeSheet",id="go_generate" ,color="primary", className="mr-1"),
        dbc.Button("Report",id='go_report', color="secondary", className="mr-1"),
        card

    ]
)

