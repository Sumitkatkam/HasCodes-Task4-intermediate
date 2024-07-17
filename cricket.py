import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Load the dataset
df = pd.read_csv('cricket.csv')

# Create Dash application
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("ICC World Cup 2007 - Indian Team Dashboard"),
    
    dcc.Graph(id='runs-scored-plot'),
    dcc.Graph(id='wickets-taken-plot'),
    dcc.Graph(id='strike-rate-plot'),
    dcc.Graph(id='batting-bowling-avg-plot')
])

# Callbacks to update plots based on user interaction (if needed)
@app.callback(
    Output('runs-scored-plot', 'figure'),
    [Input('runs-scored-plot', 'id')]
)
def update_runs_scored_plot(_):
    fig = px.bar(df, x='PlayerName', y='Runs', title='Runs Scored by Players')
    return fig

@app.callback(
    Output('wickets-taken-plot', 'figure'),
    [Input('wickets-taken-plot', 'id')]
)
def update_wickets_taken_plot(_):
    fig = px.bar(df, x='PlayerName', y='Wickets', title='Wickets Taken by Players')
    return fig

@app.callback(
    Output('strike-rate-plot', 'figure'),
    [Input('strike-rate-plot', 'id')]
)
def update_strike_rate_plot(_):
    fig = px.bar(df, x='PlayerName', y='StrikeRate', title='Strike Rates of Players')
    return fig

@app.callback(
    Output('batting-bowling-avg-plot', 'figure'),
    [Input('batting-bowling-avg-plot', 'id')]
)
def update_batting_bowling_avg_plot(_):
    fig = px.scatter(df, x='BattingAverage', y='BowlingAverage', text='PlayerName', title='Batting vs Bowling Average')
    fig.update_traces(textposition='top center')
    return fig

# Run the Dash application
if __name__ == '__main__':
    app.run_server(debug=True)
