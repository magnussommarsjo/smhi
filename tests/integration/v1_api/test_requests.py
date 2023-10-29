"""Test calls towards smhi api."""

import pytest
from smhi.api.v1 import requests as rq


def test_category() -> None:
    resp = rq.category()
    assert isinstance(resp, dict)


def test_version() -> None:
    resp = rq.version()
    assert isinstance(resp, dict)


def test_parameter() -> None:
    resp = rq.parameter(rq.Param.AIR_TEMP_HOUR)
    assert isinstance(resp, dict)


def test_station() -> None:
    resp = rq.station(rq.Param.AIR_TEMP_HOUR, station=1)
    assert isinstance(resp, dict)


@pytest.mark.skip("station_se function not implemented.")
def test_station_set() -> None:
    resp = rq.station()
    assert isinstance(resp, dict)


def test_period() -> None:
    resp = rq.period(rq.Param.GUST_WIND, station=159880, period=rq.Period.LATEST_HOUR)
    assert isinstance(resp, dict)


def test_data() -> None:
    resp = rq.data(rq.Param.GUST_WIND, station=159880, period=rq.Period.LATEST_HOUR)
    assert isinstance(resp, dict)
