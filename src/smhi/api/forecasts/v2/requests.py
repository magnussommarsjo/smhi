import httpx
import json
import enum

from .models import ApprovedTime, ValidTime

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
