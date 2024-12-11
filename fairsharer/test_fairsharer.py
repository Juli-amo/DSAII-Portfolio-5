import pytest
from fairsharer.fair_sharer import fair_sharer

def test_positive_numbers():
    assert fair_sharer([200, 1000, 800, 10], 1) == [300, 800, 900, 10]
