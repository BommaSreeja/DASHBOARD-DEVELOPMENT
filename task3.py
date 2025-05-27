import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import webbrowser
import threading

# Load the dataset
file_path = "C:/Users/sreej/Downloads/Crop_recommendation.csv"  # Adjust path
df = pd.read_csv(file_path)

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Crop Recommendation Dashboard"

# Layout of the app
app.layout = html.Div([
    html.H1("Crop Recommendation Analysis Dashboard", style={'text-align': 'center'}),
    
    html.Div([
        dcc.Dropdown(
            id='crop-dropdown',
            options=[{'label': crop, 'value': crop} for crop in df['label'].unique()],
            value=df['label'].unique()[0],
            multi=False,
            style={'width': '50%', 'margin': 'auto'}
        ),
    ], style={'text-align': 'center', 'padding': '10px'}),

    html.Div([
        dcc.Graph(id='correlation-heatmap'),
        dcc.Graph(id='rainfall-temperature'),
    ])
])

# Callback for heatmap
@app.callback(
    Output('correlation-heatmap', 'figure'),
    [Input('crop-dropdown', 'value')]
)
def update_heatmap(selected_crop):
    crop_data = df[df['label'] == selected_crop]

    # Drop non-numeric column before computing correlation
    numeric_data = crop_data.drop(columns=['label'])
    corr_matrix = numeric_data.corr()

    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='Viridis'
    ))
    fig.update_layout(
        title=f'Correlation Matrix for {selected_crop}',
        xaxis_title='Features',
        yaxis_title='Features'
    )
    return fig

# Callback for scatter plot
@app.callback(
    Output('rainfall-temperature', 'figure'),
    [Input('crop-dropdown', 'value')]
)
def update_scatter(selected_crop):
    crop_data = df[df['label'] == selected_crop]

    fig = px.scatter(
        crop_data,
        x='rainfall',
        y='temperature',
        color='label',
        title=f'Rainfall vs Temperature for {selected_crop}',
        labels={'rainfall': 'Rainfall (mm)', 'temperature': 'Temperature (°C)'}
    )
    return fig

# Automatically open the browser
def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")

# Run the app
if __name__ == '__main__':
    threading.Timer(1, open_browser).start()
    app.run(debug=True, use_reloader=False)
