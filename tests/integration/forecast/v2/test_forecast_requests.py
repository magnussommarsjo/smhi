from smhi.api.forecasts.v2 import requests as rq


def test_approved_time() -> None:
    rq.approved_time()


def test_valid_time() -> None:
    rq.valid_time()


def test_get_point_forecast() -> None:

    lat, long = 58.410130, 11.498462
    rq.get_point_forecast(long, lat)
