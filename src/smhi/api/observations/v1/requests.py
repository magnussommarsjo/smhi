import httpx
import json
import enum

BASE_URL = "https://opendata-download-metobs.smhi.se/api"
VERSION = "1.0"
_EXT = "json"


class RequestError(Exception):
    """Error for an failed request"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Period(enum.StrEnum):
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


def category() -> dict:
    """Entry point of api.

    This is the entry point of the API. Here you can select which `Version` to use.
    It is recommended to use the `Version` with the highest number to ensure a stable
    api. If you use any of the older, deprecated, versions you should upgrade.
    These are deprecated and not maintained. The Version called latest is just a
    reference to the latest `Version`. Do not use this if you are not prepared for
    changes. When a new version is published the latest version will point to the new
    version.

    References
    ----------
    http://opendata.smhi.se/apidocs/metobs/category.html
    """
    return _get_request(f".{_EXT}")


def version(version=VERSION) -> dict:
    """Get verison related information.

    This level represents a `Version` of the API. From here you can select one of the
    `Parameters` available.

    References
    ----------
    http://opendata.smhi.se/apidocs/metobs/version.html
    """
    return _get_request(f"/version/{version}.{_EXT}")


def parameter(parameter: Param, version=VERSION) -> dict:
    """Get parameter related information.

    This level represents a `Parameter` in the API. In the list of available `Stations`
    you can find out the latest position of the `Station`. There is also links to any
    `Station Set` valid for this parameter.


    References
    ----------
    http://opendata.smhi.se/apidocs/metobs/parameter.html
    """
    # TODO: Add measureing stations filter ?measuringtations={measuringStations}
    return _get_request(f"/version/{version}/parameter/{parameter}.{_EXT}")


def station(parameter: Param, station: int, version=VERSION) -> dict:
    """Get information of the station.

    This level represents a `Station` in the API. Notice that in addition to the regular
    information there also is information about the latest position of the `Station`.
    From here you can select what `Period` you are interested in.

    References
    ----------
    http://opendata.smhi.se/apidocs/metobs/station.html
    """
    return _get_request(
        f"/version/{version}/parameter/{parameter}/station/{station}.{_EXT}"
    )


def station_set() -> dict:
    """Get information of a station set.

    This level represents a `Station Set` in the API. From here you can select what
    `Period` you are interested in.

    If a station is missing data you get an empty array as value, "value": [], in the
    JSON answer.

    References
    ----------
    http://opendata.smhi.se/apidocs/metobs/stationSet.html
    """
    raise NotImplementedError


def period(parameter: Param, station: int, period: Period, version=VERSION) -> dict:
    """Get information of the period.

    This level represents a Period`` in the API. Here you can find links to the actual
    `Data`. Make sure to check the updated timestamp which indicates if new `Data` is
    available. If the timestamp is the same as the last time you requested `Data`, then
    there is no use downloading it again.

    References
    ----------
    http://opendata.smhi.se/apidocs/metobs/period.html
    """
    # TODO: There are two diffrent api calls to this. One with station-set as well.
    # Implement this!
    return _get_request(
        f"/version/{version}/parameter/{parameter}/station/{station}/period/{period}.{_EXT}"
    )


def data(parameter: Param, station: int, period: Period, version=VERSION) -> dict:
    """Get data.

    The final level of the API is the `Data` level. This is where you get the actual
    `Data`. Notice that data is only available in CSV format for the `Period`
    corrected-archive, but also available in XML and JSON for the rest of the `Periods`.

    All dates in the JSON answers are in Unix time stamp.

    NB: For station-set, if a station is missing data you get "value": null in the JSON
    answer.

    References
    ----------
    http://opendata.smhi.se/apidocs/metobs/data.html
    """

    if period == Period.CORRECTED_ARCHIVE:
        # TODO: Implementation of csv parsing needed.
        raise NotImplementedError("Parsing csv files is not supported.")

    # TODO: Also implement station-set call. This will also result in diffrent output
    # that needs testing.

    # NOTE: We can get 4 diffrent output sets. and needs to be implemented correctly.
    # - CSV(station)
    # - JSON(station)
    # - CSV(station set)
    # - JSON(station-set)

    return _get_request(
        f"/version/{version}/parameter/{parameter}/station/{station}/period/{period}/data.{_EXT}"
    )
