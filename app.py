import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, MATCH
import plotly.express as px

app = dash.Dash(__name__)

# 2つのコンポーネントを持つレイアウト

app.layout = html.Div(
    [
        html.Button("ここを押す", id="test_2"),
        html.Div(id="test_1", children=[]),
    ]
)

@app.callback(
    Output("test_1", "children"),
    Input("test_2", "n_clicks"),
    State("test_1", "children"),
    prevent_initial_call = True
)
def add_dropbox(n_clicks, children):
    new_layout = html.Div(
        [
            html.H1(id="my_text_1"),
            html.Div(
                dcc.Dropdown(
                    id = "word_selector_1",
                    options = [
                        {"label": "東京", "value": "tokyo"},
                        {"label": "京都", "value": "kyoto"},
                    ],
                    value = "tokyo"
                )
            ),
            html.Div(
                dcc.Dropdown(
                    id = "word_selector_2",
                    options = [
                        {"label": "新宿", "value": "sinjuku"},
                        {"label": "難波", "value": "nanba"},
                    ],
                    value = "sinjuku"
                )
            )
        ]
    )
    children = new_layout
    return children

@app.callback(
    Output("my_text_1", "children"),
    Input("word_selector_1", "value"),
    Input("word_selector_2", "value"),
    prevent_initial_call = True
)
def update_words(select_word_1, select_word_2):
    return str(select_word_1) + str(select_word_2)

app.run_server(debug=True)