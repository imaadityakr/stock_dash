import pandas_datareader.data as web
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import datetime
import pandas as pd
import dash_bootstrap_components as dbc
import  plotly.express as px

from dash import Dash
from dash_extensions import Lottie
import nsetools



from nsetools import Nse
nse = Nse()
url_connections = "https://assets2.lottiefiles.com/packages/lf20_xa4vkunf.json"

url_companies = "https://assets1.lottiefiles.com/packages/lf20_z10xyyny.json"

url_msg1= "https://assets10.lottiefiles.com/private_files/lf30_1l8zkdv6.json"

url_stock2= "https://assets5.lottiefiles.com/packages/lf20_wvntgftp.json"

url_profit ="https://assets4.lottiefiles.com/private_files/lf30_qKbFdb.json"

options = dict(loop =True,autoplay = True,rendererSettings=dict(preservesAspectRatio='xMidYMid slice'))

app = Dash(__name__,external_stylesheets=[dbc.themes.SOLAR])
server = app.server

app.layout= dbc.Container([
#row 1
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardImg(src='https://www.sabertoothtech.in/static/images/SabertoothLogo.png')
            ],className='mb-2'),

        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.DatePickerSingle(
                        id='my-date-picker-start',
                        date=datetime.date(2018,1,1),
                        className='ml-5'
                    ),
    dcc.DatePickerSingle(
                        id='my-date-picker-end',
                        date=datetime.date.today(),
                        className='mb-2 ml-2'
                    ),
                    dcc.Input(
                        id="stock_name", value='TSLA', type='text',

                        className='ml-5 mb-2'
                    ),


                ])
            ]),

        ], width=8),
    ],className='mb-2 mt-2'),

 #row 2.1
dbc.Row([
        dbc.Col([
            dbc.Card([
                    dbc.CardHeader(Lottie(options=options, width="100%", height="120%", url=url_companies)),
                    dbc.CardBody([
                        html.H6(id="Companies",children=""),
                        html.H2(id="content-companies", children="")

                    ], style={'textAlign': 'center'}),

                ])
            ], width=2),


dbc.Col([
            dbc.Card([
                    dbc.CardHeader(Lottie(options=options, width="40%", height="15%", url=url_connections)),
                    dbc.CardBody([
                        html.H6(id="Connections",children=""),
                        html.H2(id="content-connections", children="0000")

                    ], style={'textAlign': 'center'}),

                ])
            ], width=2),
dbc.Col([
            dbc.Card([
                    dbc.CardHeader(Lottie(options=options, width="40%", height="15%", url=url_msg1)),
                    dbc.CardBody([
                        html.H6(id="Stocks",children=""),
                        html.H2(id="content-stock", children="0000")

                    ], style={'textAlign': 'center'}),

                ])
            ], width=2),

dbc.Col([
            dbc.Card([
                    dbc.CardHeader(Lottie(options=options, width="40%", height="15%", url=url_stock2)),
                    dbc.CardBody([
                        html.H6(id="Market",children=""),
                        html.H2(id="content-market", children="0000")

                    ], style={'textAlign': 'center'}),

                ])
            ], width=2),

dbc.Col([
            dbc.Card([
                    dbc.CardHeader(Lottie(options=options, width="29%", height="15%", url=url_profit)),
                    dbc.CardBody([
                        html.H6(id="Profit",children=""),
                        html.H2(id="content-profit", children="0000")

                    ], style={'textAlign': 'center'}),

                ])
            ], width=2),

    ],className='mb-2'),

    #row 2
dbc.Row([
        dbc.Col([
            dbc.Card([

                dbc.CardBody([
                    dcc.Graph(id='line-chart',figure={})
                    #html.H2(id="content-companies",children="0000")

                ])
            ])
        ], width=5),
dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='bar-chart',figure={})
                ])
            ])
        ], width=5)
    ],className='mb-2'),
    #row 3
# dbc.Row([
#         dbc.Col([
#             dbc.Card([
#                 dbc.CardBody([
#                         dcc.Graph(id='pie-chart',figure={}, style={'backgroundColor': 'teal'})
#                 ])
#             ])
#         ], width=5),
# dbc.Col([
#             dbc.Card([
#                 dbc.CardBody([
#                         dcc.Graph(id='donught-chart',figure={}, style={'backgroundColor': 'teal'})
#                 ])
#             ])
#         ], width=5)
#     ] ,className='mb-2')
#     #row 4
],fluid=True)


@app.callback(
    Output(component_id="line-chart" ,component_property='figure'),
    Output(component_id="content-companies" ,component_property='children'),
    Output(component_id="Companies" ,component_property='children'),
    Output(component_id="bar-chart" ,component_property='figure'),
    Output(component_id="Connections" ,component_property='children'),
    Output(component_id="content-connections" ,component_property='children'),
    Output(component_id="Stocks" ,component_property='children'),
    Output(component_id="content-stock" ,component_property='children'),
    Output(component_id="Market" ,component_property='children'),
    Output(component_id="content-market" ,component_property='children'),
    Output(component_id="Profit" ,component_property='children'),
    Output(component_id="content-profit" ,component_property='children'),
    [Input(component_id="stock_name", component_property='value'),
     Input(component_id="my-date-picker-start", component_property='date'),
     Input(component_id="my-date-picker-end", component_property='date')]

)
def update_value(input_data,start_date,end_date):
    start = start_date
        #datetime.datetime(2010, 1, 1)
    end = end_date
    df1 = web.DataReader(input_data, 'yahoo', start, end)
    df1=df1.reset_index()
    figure = px.line(df1, x='Date', y='Close',title=input_data)
    figure.update_traces(marker_color='green',
                      marker_line_width=1.5)
    figure.update_layout(
        plot_bgcolor="#1E434A",
        paper_bgcolor="#1E434A",
        font_color="white"
    )


    # figure={'data': [{'x': df.index, 'y': df.Close, 'type': 'line', 'name': input_data},],
    #                                     'layout': {'title': input_data,'plot_bgcolor':"#1E434A","paper_bgcolor":"#1E434A",
    #                                                "font_color":"#004510"},
    #
    # }


    #figure.layout.plot_bgcolor = '#fff'

    top_gainers = nse.get_top_gainers()

    sample=top_gainers
    df=pd.DataFrame.from_dict(top_gainers)


    fig = px.bar(df,x='symbol',y='openPrice',title="Top Gainer")
    fig.update_traces(marker_color='rgb(255,165,0)', marker_line_color='rgb(8,48,107)',
                      marker_line_width=1.5)
    fig.update_layout(
        plot_bgcolor="#1E434A",
        paper_bgcolor="#1E434A",
        font_color="white"
    )

    print(sample[-1]['symbol'])

    child= str(sample[-1]['openPrice'])
    name= str(sample[-1]['symbol'])
    #
    Connections = str(sample[-2]['symbol'])
    Connections1 = str(sample[-2]['openPrice'])

    Stocks = str(sample[-3]['symbol'])

    Stocks1 = str(sample[-3]['openPrice'])

    Market = str(sample[-4]['symbol'])
    #
    Market1 = str(sample[-4]['openPrice'])

    Profit = str(sample[-5]['symbol'])
    #
    Profit1 = str(sample[-5]['openPrice'])




    return figure ,child ,name,fig ,Connections,Connections1,Stocks,Stocks1,Market,Market1,Profit,Profit1

if __name__ == '__main__':

    app.run_server(debug=True)