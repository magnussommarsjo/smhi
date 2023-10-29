import pytest
import json


@pytest.fixture
def parameter_response() -> dict:
    with open("tests/fixtures/parameter_response.json", "r") as file:
        return json.load(file)


@pytest.fixture
def category_response() -> dict:
    with open("tests/fixtures/category_response.json", "r") as file:
        return json.load(file)


@pytest.fixture
def version_response() -> dict:
    with open("tests/fixtures/version_response.json", "r") as file:
        return json.load(file)
