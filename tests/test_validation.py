from sgmc.generation import generate_valid_solution, random_solution
from sgmc.validation import validate_solution


def test_random():
    # This is highly unlikely
    assert not all(validate_solution(random_solution()) for i in range(10))


def test_valid():
    assert validate_solution(generate_valid_solution())
