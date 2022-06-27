from demo_code import RandomNumberGenerator
import assignment


def test_random_number_generator():
    """Test random number generator."""
    assert RandomNumberGenerator().get_number()

    if False:
        assert "Dead Code!"
        print ("Gotcha!")
