from smhi.api.v1 import models


def test_parameter_response(parameter_response: dict) -> None:
    models.ParameterResponse(**parameter_response)
    # If we get here we suceeded in parsing


def test_category_response(category_response: dict) -> None:
    models.CategoryResponse(**category_response)
