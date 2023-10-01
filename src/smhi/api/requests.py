import httpx
import json
import enum

BASE_URL = "https://opendata-download-metobs.smhi.se/api"
VERSION = "latest"
_EXT = "json"


class RequestError(Exception):
    """Error for an failed request"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Period(str, enum.Enum):
    LATEST_HOUR = "latest-hour"
    LATEST_DAY = "latest-day"
    LATEST_MONTHS = "latest-months"
    CORRECTED_ARCHIVE = "corrected-archive"


class Param(enum.IntEnum):
    """Parameters definition.

    Notes
    -----
    Not a complete list

    References
    ----------
    http://opendata.smhi.se/apidocs/metobs/parameter.html
    """

    GUST_WIND = 21
    DEW_POINT_TEMP = 39
    AIR_TEMP_DAY_AVG = 2
    AIR_TEMP_HOUR = 1
    WIND_SPEED_AVG_HOUR = 4
    WIND_DIRECTION_HOUR = 3


def _get_request(endpoint: str) -> dict:
    """Get a response from endpoint and parse it to python dict."""
    url = BASE_URL + endpoint
    response = httpx.get(url)
    if not response.is_success:
        raise RequestError(
            f"Failed with status code {response.status_code} when calling {url}"
        )

    return json.loads(response.text)


def abut() -> dict:
    return _get_request(f".{_EXT}")


def version(version=VERSION) -> dict:
    return _get_request(f"/version/{version}.{_EXT}")


def parameter(parameter: Param, version=VERSION) -> dict:
    return _get_request(f"/version/{version}/parameter/{parameter}.{_EXT}")