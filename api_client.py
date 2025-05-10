import os
import requests
import json
from mock_api import mock_tfl_response
with open("stop_configuration.json") as f:
    STOPS = json.load(f)

app_id = os.environ.get("TFL_APP_ID")
app_key = os.environ.get("TFL_APP_KEY")
use_mock_api = os.environ.get("USE_MOCK_API", "false").lower() == "true"

def get_bus_arrivals():
    all_arrivals = []

    for stop_name, stop_data in STOPS.items():
        stop_id = stop_data['id']
        url = f"https://api.tfl.gov.uk/StopPoint/{stop_id}/Arrivals"
        params = {"app_id": app_id, "app_key": app_key}
        resp = mock_tfl_response(stop_id) if use_mock_api else requests.get(url, params=params)
        data = resp.json()

        all_arrivals.extend([
            f"Bus {d['lineName']} at {stop_name} in {int(d['timeToStation'] / 60)}min"
            for d in data
            if d["lineName"] in stop_data["lines"]
        ])

    return sorted(all_arrivals)
