import assignment
from demo_code import RandomNumberGenerator


def test_random_number_generator():
    """Test random number generator."""
    assert RandomNumberGenerator().get_number()

    if False:
        assert "Dead Code!"
        print("Gotcha!")


def test_partial_code():
    """Some test to check the new metric."""
    assert assignment.tested_foo() == 5
