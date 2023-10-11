from smhi import models


def test_parameter_response(parameter_response: dict) -> None:
    models.ParameterResponse(**parameter_response)
    # If we get here we suceeded in parsing
