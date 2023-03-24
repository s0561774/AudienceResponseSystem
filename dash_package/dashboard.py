from dash import Input, Output, State, Dash, html, dcc
import dash_bootstrap_components as dbc
from pandas import DataFrame
import plotly.express as px
from dash_package import app
from . import ids
from dash_package.functions import get_data_for_chart, get_question_for_chart

datas = get_question_for_chart()

header_row_1 = dbc.Row( children=[
html.H1("Questions & Answers",   className="display-3", style={'fontWeight':'Bold'}),
            
            html.P(
                "This application is a simple pools, which allows a user to create a questions and to show the result in a diagram."
            ),
])
nav = dbc.Nav(
    [
        dbc.NavLink("Home",  href="/",  external_link=True),
        dbc.NavLink("Questions", href="/pools", external_link=True),
        dbc.NavLink("Results",active=True, href="/dashApp")
    ]
)
header_row_2 = dbc.Row( children=[
        dbc.Nav( children=[
            nav
        ])
])

jumbotron = html.Div(
    dbc.Container(
        [
            header_row_1,
            html.Hr(className="my-2"),
            header_row_2       
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-light rounded-3",
)
types_diagrams =["Pie Chart", "Histogram", "Box Plot"]

row_1 = dbc.Row(
    [
      
        dbc.Col(
            html.Div(
                children=[
                    html.H6("Question"),
                    dcc.Dropdown(
                        id= ids.LISTE_QUESTION,
                        options=[{"label": elt[3], "value":elt[1]} for elt in datas],
                         
                    ),
                   
                ]
            )
        )
    ]
)
row_2 = dbc.Row(
    children=[
        dbc.Col(
        html.Div(
            id=ids.GRAPH
        ), width= 8
        ),
         dbc.Col(
            id=ids.CORRECT_ANSWER,
            children = [
                    html.Br(),
                    html.Div([
                        dbc.Button(id=ids.SHOW_ANSWER ,children=["Show correct answers"], color="primary", className="me-1"),
                        ], 
                    ),
                    html.Div([html.Br()]),
                    html.Div( id= ids.BLOCK_ANSWER
                    )
            ], width=4, style={'display':'none' }
        )
    ]
    
)


app.layout = dbc.Container(style={'padding':'10px', 'height': '100vh' ,
         'boxShadow':'inset 0 -3em 3em rgba(0, 0, 0, 0.1), 0 0 0 2px rgb(255, 255, 255), 0.3em 0.3em 1em rgba(0, 0, 0, 0.3)'                         }, 

    children=[
            jumbotron,
            html.Br(),
            row_1,
            row_2

         ]
    )


# Callback für Generierung von Graphen
@app.callback(
    Output(ids.GRAPH, "children"),
    Input(ids.LISTE_QUESTION, 'value')
)
def generate_graph(val):
    if val is not None:
        global dt
        dt = get_data_for_chart(val)
        dfr = DataFrame({"Answers": dt[0], "Values":dt[2]})
        #fig = px.pie(dfr, values='Values', names='Answers')
        fig = px.bar(x = dt[0], y =dt[2] )
        #fig = px.histogram(dfr, x="Answers", y= "Values", color="Answers")
        return dcc.Graph(figure=fig)

@app.callback(
    Output(ids.CORRECT_ANSWER, "style"),
    Input(ids.LISTE_QUESTION, 'value')
)
def activate_button(val):
    if val is not None:
        return {'display': 'block'}
    else:
        return {'display': 'none'}

@app.callback(
    Output(ids.BLOCK_ANSWER, "children"),
    Input(ids.SHOW_ANSWER, 'n_clicks'),
     prevent_initial_call=True
)
def show_answers(n_clicks):
    list_group = dbc.ListGroup([])
    print(dt)
    for elt in dt[0]:
        if elt not in dt[1]:
            list_group.children.append(dbc.ListGroupItem(elt))
        else:
            list_group.children.append(dbc.ListGroupItem(elt, color="success"))
    return list_group
