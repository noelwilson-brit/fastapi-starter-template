import json
import os
import pytest
from app.core.calculations import basic_rater


@pytest.fixture
def test_data():
    return {"test": "test_data"}


@pytest.fixture
def create_test_file(test_data):
    with open("test_data.json", "wb") as fp:
        fp.write(json.dumps(test_data).encode())
    
    yield "test_data.json"

    os.remove("test_data.json")


@pytest.mark.parametrize("input_value, expected_result", [
    ("2", 4),
    (2, 4),
    (1, 2),
    (0, 0),
    (-2, -4)
])
def test_basic_rater(create_test_file, input_value, expected_result):
    assert basic_rater(input_value) == expected_result
    