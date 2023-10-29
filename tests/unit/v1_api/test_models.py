from smhi.api.v1 import models


def test_parameter_response(parameter_response: dict) -> None:
    models.ParameterResponse(**parameter_response)
    # If we get here we suceeded in parsing


def test_category_response(category_response: dict) -> None:
    models.CategoryResponse(**category_response)


def test_version_response(version_response: dict) -> None:
    models.VersionResponse(**version_response)


def test_station_response(station_response: dict) -> None:
    models.StationResponse(**station_response)


def test_station_set_response(station_set_response: dict) -> None:
    models.StationSetResponse(**station_set_response)
