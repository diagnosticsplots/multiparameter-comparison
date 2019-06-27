import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import flask
from flask_cors import CORS
import os


#Main app
app = dash.Dash()

#layout for Input
app.layout=html.Div([ #main page

    html.Div([ # Input section
        html.Table([ #Input 2x2 design table
            html.Tr([
                #First row requests the name of the first variable
                html.Th([
                        dcc.Input(
                            id='name1',
                            type='text',
                            value='Variable1',
                        ),
                ], colSpan='4', style={'text-align':'center'}),
            ]),
            html.Tr([
                #second row with the input for the vertical variable
                html.Th([
                    dcc.Input(
                        id='name2',
                        type='text',
                        value='Variable2',
                    ),
                ], rowSpan='3'),
                html.Th(['']),
                html.Th(['-1']),
                html.Th(['+1']),
            ]),
            html.Tr([
                #Third row with the inputs of lolo and lohi
                html.Th(['-1']),
                html.Td([
                    dcc.Input(
                        id="lolo",
                        type='number',
                        value='5'
                    )
                ]),
                html.Td([
                    dcc.Input(
                        id="lohi",
                        type='number',
                        value='10'
                    )
                ]),
            ]),
            html.Tr([
                html.Th(['+1']),
                html.Td([
                    dcc.Input(
                        id="hilo",
                        type='number',
                        value='15'
                    )
                ]),
                html.Td([
                    dcc.Input(
                        id="hihi",
                        type='number',
                        value='20'
                    )
                ]),
            ]),
        ], className='table'),
    ]),
    #Output section
    html.Div(dcc.Graph(id='main-graph-out'),style={'text-align':'center'}),
])

#mechanics
@app.callback(
    Output(component_id='main-graph-out', component_property='figure'),
    [
        Input(component_id='lolo',component_property='value'),
        Input(component_id='lohi',component_property='value'),
        Input(component_id='hilo',component_property='value'),
        Input(component_id='hihi',component_property='value'),
        Input(component_id='name1', component_property='value'),
        Input(component_id='name2', component_property='value'),
    ]
)
def update_graph(lolo, lohi, hilo, hihi,var1, var2):
    matrix = [[lolo, lohi],
              [hilo, hihi]]
    data =[
        go.Contour(
            z=matrix,
            x=[-1, 1],
            y=[-1, 1],
            colorscale='Greys',
            contours=dict(
                coloring='lines',
                showlabels=True,
                labelfont=dict(
                    family='Raleway',
                    size=16,
                    color='black',
                ),
            ),
            showscale=False,
            autocontour=False,
            ncontours=25,
            line=dict(
                width=2,
                smoothing=0.5,
            ),
        ),
    ]
    layout = go.Layout(
        autosize=False,
        width=600,
        height=600,
        margin=dict(
            l=100,
            r=100,
            b=100,
            t=100,
            pad=10
        ),
        xaxis=dict(
            title=var1,
            range=[-1.5, 1.5],
            tick0=0,
            dtick=1,
            zeroline=False,
        ),
        yaxis=dict(
            title=var2,
            range=[-1.5, 1.5],
            tick0=0,
            dtick=1,
            zeroline=False,
        ),
        shapes=[
            dict(
                type='rect',
                x0=-1,
                y0=-1,
                x1=1,
                y1=1,
            ),
        ],
    )
    return {'data': data, 'layout':layout}

external_css = [
    #"https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",  # Normalize the CSS
    "https://fonts.googleapis.com/css?family=Open+Sans|Roboto",  # Fonts
    "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
    "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css",
    "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css",
    "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js",
    ]

for css in external_css:
    app.css.append_css({"external_url": css})



if __name__ == '__main__':
    app.run_server(debug=True)
