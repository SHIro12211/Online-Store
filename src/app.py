#code for dash and plotly
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
import sys
sys.path.append("src\\scripts")
import data_loader
import utils

data= data_loader.load_data("dataset/processed/sales_data_cleaned.csv", True)

#Create dropdown menu option
dropdown_options=[
    {'label': 'Graph 1', 'value': 1},
    {'label': 'Graph 2', 'value': 2},
    {'label': 'Graph 3', 'value': 3}
]
#Initialize the Dash app
app= dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create the layout of the app
app.layout=dbc.Container(
    [
    html.H1("📊 Sales Dashboard", className="my-4 text-center"),
    dbc.Row([
        dbc.Col([
            html.Label('Select a Graph'),
            dcc.Dropdown(
                id='select-graph',
                options=dropdown_options,
                placeholder="Select a graph",
                className="mb-4"
            )
        ], width=3)
    ]),
    dbc.Row(id='output-container', class_name='g-4') #space between columns
    ],
    style={"maxWidth": "1600px", "margin": "0 auto"}
)
@app.callback(
    Output('output-container', 'children'),
    Input('select-graph', 'value')
)
def update_graphs(selected_option):
    data_2023 = data[data.index.year == 2023].copy()
    df_1, df_2, df_3 = utils.get_group_data(data_2023)
    color_palette = ["#41668D", "#A0CBE8", '#F28E2B', '#FFBE7D', '#59A14F', '#8CD17D', '#B6992D', '#499894']

    if selected_option == 1:
        fig1 = px.bar(df_1, x='Product Category', y='Total Amount', color='Product Category',
                      title='💰 Profit by Product Category', color_discrete_sequence=color_palette)

        fig1.update_layout(yaxis_tickprefix="$")

        fig2 = px.bar(df_1, x='Product Category', y='Quantity', color='Product Category',
                      title='📦 Sales by Product Category', color_discrete_sequence=color_palette)

    elif selected_option == 2:
        fig1 = px.line(df_2, x='Month', y='Total Amount', color='Product Category',
                       title='📈 Monthly Profit by Product Category',  color_discrete_sequence=color_palette)
        fig1.update_layout(yaxis_tickprefix="$")

        fig2 = px.line(df_2, x='Month', y='Quantity', color='Product Category',
                       title='📈 Monthly Sales by Product Category',  color_discrete_sequence=color_palette)
        
    elif selected_option == 3:
        fig1 = px.bar(df_3, x='Gender', y='Total Amount', color='Product Category', barmode="group",
                      title='💰 Profit by Gender and Category',  color_discrete_sequence=color_palette)
        fig1.update_layout(yaxis_tickprefix="$")

        fig2 = px.bar(df_3, x='Gender', y='Quantity', color='Product Category', barmode="group",
                      title='📦 Sales by Gender and Category',  color_discrete_sequence=color_palette)

    return [
        dbc.Col(dcc.Graph(figure=fig1), width=6),
        dbc.Col(dcc.Graph(figure=fig2), width=6)
    ]
#Run the Dash app
if __name__ == '__main__':
    app.run()