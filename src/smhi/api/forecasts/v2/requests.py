import httpx
import json
import enum

from .models import ApprovedTime, ValidTime, PointForecast

BASE_URL = "https://opendata-download-metfcst.smhi.se/api"
VERSION = "2"


class Category(enum.StrEnum):
    PM3PG = "pmp3g"


def _get_request(endpoint: str) -> dict:
    """Get a response from endpoint and parse it to python dict."""
    url = BASE_URL + endpoint
    response = httpx.get(url)
    response.raise_for_status()
    return json.loads(response.text)


def approved_time(category: Category = Category.PM3PG) -> ApprovedTime:
    """Approved time

    To check the current forecast approved time (the time of the most recent forecastupdate),
    poll https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/approvedtime.json
    (with category and version of your choice). In the answer you get the approved time,
    which is the time when the meteorologist approved the calculated forecast, and the
    reference time, which is the time when the forecast was calculated (the start time
    for the forecast). Normally, a new forecast is approved once every hour, but notice 
    that there can be occasions that differ.
    """

    data = _get_request(f"/category/{category}/version/{VERSION}/approvedtime.json")
    return ApprovedTime(**data)


def valid_time(category: Category = Category.PM3PG) -> ValidTime:
    """Valid time

    To check the valid times for the current forecast, you can use 
    https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/validtime.json 
    (with category and version of your choice). In the answer you get the valid time list.
    You can use the answers to specify what valid time to ask for in the MultiPoint request.
    """
    data = _get_request(
        f"/category/{category}/version/{VERSION}/validtime.json"
    )
    return ValidTime(**data)


def get_point_forecast(longitude: float, latitude: float, category: Category = Category.PM3PG) -> PointForecast:
    """Get point forecast
    
    The main functionality of the API. The API response is a complete forecast approximately
    10 days ahead of the latest current forecast. All times in the answer are given in UTC.

    The data is returned as JSON, mediatype: application/json. In the JSON-result you can
    find the grid point longitude and latitude as a GeoJSON Point. This is the nearest grid
    point to the point you asked for. You can also find the referenceTime (forecast start time) 
    and the approvedTime (the time the meteorologist approved the forecast). In the timeSeries
    block you find the data for the forecast. The validTime attribute gives the time for
    when the data is valid. All parameters except the precipitation parameters has an instantaneous
    valid time. Precipitation parameters have a distribution in time (a time interval)
    until the valid time for current data. The interval starts at the time step before.
    At the beginning of the forecast, the interval is one hour. Later in the forecast,
    the time interval increases (eg 3, 6 and 12 h). Unit remains mm / h. After the validTime
    attribute all the Parameters and their values are listed.
    """

    data = _get_request(f"/category/{category}/version/{VERSION}/geotype/point/lon/{longitude}/lat/{latitude}/data.json")
    return PointForecast(**data)

def get_multipoint_forecast():
    # TODO: Implement
    raise NotImplementedError()