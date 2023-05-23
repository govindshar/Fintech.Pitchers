import dash
import dash_core_components as dcc
import dash_html_components as html

# Create the Dash application
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div(
    children=[
        html.H1("Sales Dashboard"),
        dcc.Graph(
            id="sales-chart",
            figure={
                "data": [
                    {"x": [1, 2, 3, 4, 5], "y": [4, 6, 2, 8, 5], "type": "bar", "name": "Sales"}
                ],
                "layout": {"title": "Sales Performance"}
            }
        )
    ]
)

# Run the application
if __name__ == "__main__":
    app.run_server(debug=True)