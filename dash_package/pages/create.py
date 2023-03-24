import dash
import pandas as pd
from dash import html, dcc, Input, Output, State, ctx
import matplotlib.pyplot as plt
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

df_sheet_name = pd.read_excel('app_questions.xlsx', sheet_name='Results', header=None)
dash.register_page(
    __name__,
    path='/result',
    title='Results',
    name='Results'
)



checklist = html.Div(
    [
        dbc.Label("Choose a bunch"),
        dbc.Checklist(
            options=[
                {"label": "Pie Chart", "value": 1},
                {"label": "Histogramm", "value": 2},
            ],
            value=[1],
            id="checklist-input",
        ),
    ]
)




layout=dbc.Container([
    dbc.Row([dbc.Col(style={'marginTop': '10px'}, children=[checklist])]),
    ])

''''
@dash.callback(
    Output('answers', 'children'),
    [Input('fade-button', 'n_clicks')],
    [State('answers', 'children')],
)
def add_answer(val, children):
    if children is None:
        children = []
    if val:
        el = dbc.Card(style={'marginBottom': '10px'},
                      children=[dbc.InputGroup(id="responses" ,children=[dbc.InputGroupText(f"Option_{val}"), dbc.Input()])])
        children.append(el)
        return children
    else:
        raise PreventUpdate
@dash.callback(
    Output('diagram', 'children'),
    [Input('checklist-input', 'value')],
)
def create_diagram(val):
    if children is None:
        children = []
    if val == 2:
        
        children.append()
        return children
    else:
        raise PreventUpdate


@dash.callback(
   Output('form', 'value'),
    [Input('create-button', 'n_clicks')],
    [Input('myquestion', 'value')],
    [Input('dropdown', 'value')],
    [Input('answers', 'children')]
)
def get_data(n_clicks, dropdown,myquestion, children):
    if n_clicks:
       for childs in children:
        for child in childs.props.children:
            print(child)
        

        



@dash.callback(Output('answers', 'value'),
               Output('label', 'value'),
               Input('fade-button', 'n_clicks'),
               State('label', 'value'),
               State('answers', 'children'))
def update_output(n_clcks, questions, answers_r):
    if answers_r is None
        print(questions),
@dash.callback(
   Output('form', 'value'),
    [Input('create-button', 'n_clicks')],
    [Input('myquestion', 'value')],
    [Input('dropdown', 'value')],
    [Input('responses', 'children')],
)
def get_data(n_clicks, dropdown,myquestion, children):
    if n_clicks:
        for child in children:
            print(child.value)
        if questId is None:
        # PreventUpdate prevents ALL outputs updating
        raise dash.exceptions.PreventUpdate


'''


