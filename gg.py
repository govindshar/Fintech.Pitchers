import dash
import dash_core_components as dcc
import dash_html_components as html

# Create the Dash application
app = dash.Dash(__name__)

# Initialize an empty list to store the charts
charts = []

# Define a function to add a new chart
def add_chart():
    chart = dcc.Graph(
        id=f"chart-{len(charts) + 1}",
        figure={
            "data": [{"x": [1, 2, 3], "y": [3, 1, 2], "type": "bar"}],
            "layout": {"title": f"Chart {len(charts) + 1}"}
        }
    )
    charts.append(chart)

# Define the layout of the dashboard
app.layout = html.Div(
    children=[
        html.H1("Dynamic Chart Dashboard"),
        html.Button("Add Chart", id="add-chart-button", n_clicks=0),
        html.Div(id="chart-container")
    ]
)

# Define a callback to add a new chart when the button is clicked
@app.callback(
    dash.dependencies.Output("chart-container", "children"),
    [dash.dependencies.Input("add-chart-button", "n_clicks")]
)
def update_chart(n_clicks):
    for _ in range(n_clicks):
        add_chart()
    return charts

# Run the application
if __name__ == "__main__":
    app.run_server(debug=True)
