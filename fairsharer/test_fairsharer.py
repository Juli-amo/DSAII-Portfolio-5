import pytest
from fair_sharer import fair_sharer

# @pytest.mark.parametrize("positive_input, positive_output",
#                          [([200, 1000, 800, 10], [300, 800, 900, 10]),
#                           ([200, 201, 202, 199], [200, 221.2, 161.6, 219.2])])
def test_positive_numbers():
    assert fair_sharer([200, 1000, 800, 10], 1) == [300, 800, 900, 10]


# @pytest.mark.parametrize("negative_input, negative_output",
#                          [([-200, -1000, -800, -10], [-199, -1000, -799, -12]),
#                           ([-200, -201, -202, -199], [-180.1, -201, -182.1, -238.8])])
# def test_negative_numbers(negative_input, negative_output):
#     assert fair_sharer() == negative_output


# @pytest.mark.parametrize("mixed_input, mixed_output",
#                          [([-200, 1000, -800, 10], [-100, 800, -700, 10]),
#                           ([200, -201, 202, -199], [200, -180.8, 161.6, -178.8])]) 
# def test_mixed_numbers(mixed_input, mixed_output):
#     assert fair_sharer() == mixed_output
