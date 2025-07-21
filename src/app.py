#code for dash and plotly
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import sys
sys.path.append("src\\scripts")
import data_loader
import utils

data= data_loader.load_data("dataset/processed/sales_data_cleaned.csv", True)
#Create dropdown menu option
dropdown_options=[
    {
        'label':'Graph 1',
        'value':1
    },
    {
        'label':'Graph 2',
        'value':2
    },
    {
        'label':'Graph 3',
        'value':3
    }
]
#Initialize the Dash app
app= dash.Dash(__name__)

# Create the layout of the app
app.layout=html.Div(
    [
        html.H1("Dash Test A"),
        html.Div([
            html.Label('Select a Graph'),
            dcc.Dropdown(
                id='select-graph',
                options=dropdown_options,
                value='Select a Graph'
            ),
           
        ], style={'with':'50%'}),
        html.Div(id='output-container',className='chart-grid', style={'dispaly':'flex'})
        
    ]
)
@app.callback(
    Output(component_id='output-container', component_property='children'),
    Input(component_id='select-graph', component_property='value')
)
def tst(selected_option):
    data_2023=data[data.index.year==2023].copy()    
    df_1, df_2, df_3 = utils.get_group_data(data_2023)
    if selected_option == 1:
        graph_1=dcc.Graph(figure=px.bar(df_1, x='Product Category', y='Total Amount', color='Product Category', title='Total of profit by product category'))
        graph_2=dcc.Graph(figure=px.bar(df_1, x='Product Category', y='Quantity', color='Product Category', title='Total of sales by product category'))
    elif selected_option == 2:
        graph_1=dcc.Graph(figure=px.line(df_2, x='Month', y='Total Amount', color='Product Category', title='Total of profit by product category'))
        graph_2=dcc.Graph(figure=px.line(df_2, x='Month', y='Quantity', color='Product Category', title='Total of sales by product category'))
    elif selected_option == 3:
        graph_1=dcc.Graph(figure=px.bar(df_3, x='Gender', y='Total Amount', color='Product Category', barmode="group", title='Total of profit by product category'))
        graph_2=dcc.Graph(figure=px.bar(df_3, x='Gender', y='Quantity', color='Product Category', barmode="group", title='Total of sales by product category'))
    return html.Div(children=[html.Div(children=graph_1),html.Div(children=graph_2)],style={'display': 'flex'})
#Run the Dash app
if __name__ == '__main__':
    app.run()