import pytest
from app.core.calculations import basic_rater

@pytest.fixture
def create_test_file():
    with open("test_data.json", "wb") as fp:
        fp.write('{"test": "test_data"}'.encode())
    
    return "test_data.json"


@pytest.mark.parametrize("input_value, expected_result", [
    ("2", 4),
    (2, 4),
    (1, 2),
    (0, 0),
    (-2, -4)
])
def test_basic_rater(create_test_file, input_value, expected_result):
    assert basic_rater(input_value) == expected_result
    