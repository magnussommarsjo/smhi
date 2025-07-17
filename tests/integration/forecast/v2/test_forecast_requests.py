from smhi.api.forecasts.v2 import requests as rq


def test_approved_time() -> None:
    rq.approved_time()


def test_valid_time() -> None:
    rq.valid_time()
