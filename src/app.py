from dash import Dash, dash_table, html, dcc, Input, Output, State, ctx
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from scipy.stats import beta
import numpy as np
import pandas as pd
from dash.exceptions import PreventUpdate
import json



app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB,'.assets/custom.css'])
server = app.server
percentage_format = dash_table.FormatTemplate.percentage(0)
#formatting

# app.config.suppress_callback_exceptions=True

#     fig.update_layout(showlegend=True)


# html components




heading = html.H4(
    "DietPy", className="bg-primary text-white p-2"
)
micro_summary_table = html.Div(id='micro-summary-table')

# define panels
control_panel = dbc.Card(
    dbc.CardBody(
        [
         html.Button('Add Row', id='editing-rows-button', n_clicks=0),
         html.Button('Save recipe', id='save-recipe-button', n_clicks=0)],
        className="bg-light",
    )
)
graph = dbc.Card(
    [dcc.Tabs([
        dcc.Tab(label='Macronutrients', children=[
                    ]),
        dcc.Tab(label='Detail View', children=[
            
        ]),

    ]) 

    ]
)

# define layout
app.layout = html.Div(
    [heading, dbc.Row([dbc.Col(control_panel, md=3), dbc.Col(graph, md=9)])]
)



if __name__ == "__main__":
    app.run_server(debug=True)

