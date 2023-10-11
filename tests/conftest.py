import pytest
import json


@pytest.fixture
def parameter_response() -> dict:
    with open("tests/fixtures/parameter_response.json", "r") as file:
        return json.load(file)
