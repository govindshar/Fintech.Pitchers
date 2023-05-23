import requests
import json

# Define the URL of the running Dash server
server_url = "http://localhost:8050"

# Define the function to append a new chart to the existing dashboard
def add_chart():
    chart_data = {
        "data": [{"x": [1, 2, 3], "y": [3, 1, 2], "type": "bar"}],
        "layout": {"title": "New Chart"}
    }
    chart_endpoint = server_url + "/_dash-update-component"
    payload = {
        "output": f"chart-{get_chart_count() + 1}",
        "props": chart_data
    }
    response = requests.post(chart_endpoint, json=payload)

    if response.status_code == 200:
        print("New chart added successfully!")
    else:
        print("Failed to add a new chart.")

# Function to get the current count of charts in the dashboard
def get_chart_count():
    layout_endpoint = server_url + "/_dash-layout"
    response = requests.get(layout_endpoint)
    if response.status_code == 200:
        layout_data = response.json()
        charts = [component for component in layout_data["props"]["children"] if component["props"]["id"].startswith("chart-")]
        return len(charts)
    else:
        return 0

# Call the add_chart() function to append a new chart to the dashboard
add_chart()
