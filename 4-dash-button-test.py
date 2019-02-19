# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import datetime
import json

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config['suppress_callback_exceptions'] = True
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

server = app.server

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    
    html.Div([
            html.Div([
                html.Button('Graph-1', id='bt1', n_clicks_timestamp='0'),
                html.Button('Graph-2', id='bt2', n_clicks_timestamp='0'),
                html.Button('Graph-3', id='bt3', n_clicks_timestamp='0'),
                html.Button('Graph-4', id='bt4', n_clicks_timestamp='0'),
    		html.Div(id='container')
			]),
	]),

     html.Div([
           html.Div([
               dcc.Graph(
                    id='example-graph'
               )
        ], className = "ten columns"),
    ]),
])

@app.callback(dash.dependencies.Output('example-graph', component_property='figure'),
 						[dash.dependencies.Input('bt1', component_property='n_clicks_timestamp'),
     					dash.dependencies.Input(component_id='bt2', component_property='n_clicks_timestamp'),
     					dash.dependencies.Input(component_id='bt3', component_property='n_clicks_timestamp'),
     					dash.dependencies.Input(component_id='bt4', component_property='n_clicks_timestamp')])
def func(bt1, bt2, bt3, bt4):
    if int(bt1) > int(bt2) and int(bt1) > int(bt3):
        e = 6
        if e == 6 and int(bt1) > int(bt4):
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
             'layout': {
                 'title': 'Dash Data Visualization 1'
                }
            }
            return figure
    elif int(bt2) > int(bt1) and int(bt2) > int(bt3):
        e = 7
        if e == 7 and int(bt2) > int(bt4):
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [1, 4, 5], 'type': 'line', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [1, 3, 6], 'type': 'bar', 'name': u'Montréal'},
                ],
             'layout': {
                 'title': 'Dash Data Visualization 2'
                }
            }
            return figure
    elif int(bt3) > int(bt1) and int(bt3) > int(bt2):
        e = 8
        if e == 8 and int(bt3) > int(bt4):
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [2, 3, 5], 'type': 'line', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [6, 7, 2], 'type': 'line', 'name': u'Montréal'},
                ],
             'layout': {
                 'title': 'Dash Data Visualization 3'
                }
            }
            return figure
    start = True
    while start and int(bt4) > int(bt1) and int(bt4) > int(bt2) and int(bt4) > int(bt3):
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [3, 4, 5], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [7, 8, 1], 'type': 'line', 'name': u'Montréal'},
            ],
         'layout': {
             'title': 'Dash Data Visualization 4'
            }
        }
        return figure
        start = False 

if __name__ == '__main__':
    app.run_server(debug=True)