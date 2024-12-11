import pytest
from fair_sharer import FairSharer

@pytest.mark.parametrize("positive_input, positive_output",
                         [([200, 1000, 800, 10], [300, 800, 900, 10]),
                          ([200, 201, 202, 199], [200, 221.2, 161.6, 219.2])])
def test_positive_numbers(positive_input, positive_output):
    fair_sharer_instance = FairSharer(positive_input, 1)
    assert fair_sharer_instance.fair_sharer() == positive_output


@pytest.mark.parametrize("negative_input, negative_output",
                         [([-200, -1000, -800, -10], [-199, -1000, -799, -12]),
                          ([-200, -201, -202, -199], [-180.1, -201, -182.1, -238.8])])
def test_negative_numbers(negative_input, negative_output):
    fair_sharer_instance = FairSharer(negative_input, 1)
    assert fair_sharer_instance.fair_sharer() == negative_output


@pytest.mark.parametrize("mixed_input, mixed_output",
                         [([-200, 1000, -800, 10], [-100, 800, -700, 10]),
                          ([200, -201, 202, -199], [200, -180.8, 161.6, -178.8])]) 
def test_mixed_numbers(mixed_input, mixed_output):
    fair_sharer_instance = FairSharer(mixed_input, 1)
    assert fair_sharer_instance.fair_sharer() == mixed_output


def test_keine_liste():
    with pytest.raises(ValueError) as error:
        FairSharer("X", 1) 
    assert "Values must be a list." in str(error.value)


def test_keine_zahlen():
    with pytest.raises(ValueError) as error:
        FairSharer(["abc"], 1)
    assert "All elements of 'values' must be numbers." in str(error.value)
