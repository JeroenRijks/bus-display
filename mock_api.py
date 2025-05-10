def mock_tfl_response(stop_id=None):
    class MockResponse:
        def __init__(self, stop_id):
            self.stop_id = stop_id

        def json(self):
            if self.stop_id == "490005919S":
                return [{
                            "lineId": "137",
                            "lineName": "137",
                            "destinationName": "Clapham Common",
                            "timeToStation": 180,
                            "expectedArrival": "2025-05-10T07:35:00Z",
                            "platformName": "Stop W"
                        },
                        {
                            "lineId": "345",
                            "lineName": "345",
                            "destinationName": "Clapham Common",
                            "timeToStation": 400,
                            "expectedArrival": "2025-05-10T07:35:00Z",
                            "platformName": "Stop W"
                        }
                    ]
            elif self.stop_id == "490006945N":
                return [{
                            "lineId": "35",
                            "lineName": "35",
                            "destinationName": "Clapham Common",
                            "timeToStation": 300,
                            "expectedArrival": "2025-05-10T07:35:00Z",
                            "platformName": "Stop X"
                        }
                    ]
            else:
                return []
    return MockResponse(stop_id)
