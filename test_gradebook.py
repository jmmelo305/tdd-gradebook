import pytest
from gradebook import letter_grade, is_passing, average, curved_score

# Letter_grade tests
def test_letter_grade_A ():
    assert letter_grade(95) == "A"

def test_letter_grade_F():
    assert letter_grade(45) == "F"

@pytest.mark.parametrize("score, expected",[(95, "A"),(45, "F"),])
def test_letter_grade (score, expected):
    assert letter_grade (score) == expected

def test_letter_grade_invalid_type():
    with pytest.raises(TypeError):
        letter_grade("hello")

# Is_passing tests
def test_is_passing_true():
    assert is_passing(75) == True 

def test_is_passing_false():
    assert is_passing(45) == False

def test_is_passing_invalid_type():
    with pytest.raises(TypeError):
        is_passing("passing")

# Average tests
def test_average_works():
    assert average([80, 90, 70]) == 80.0

def test_average_empty_list():
    with pytest.raises(ValueError):
        average([])

def test_average_not_a_list():
    with pytest.raises(TypeError):
        average("not a list")

def test_average_bad_items():
    with pytest.raises(TypeError):
        average([80, "ninety", 70])

# Curved Score Tests
def test_curved_score_basic():
    assert curved_score(80, 5) == 85.0

def test_curved_score_cap():
    assert curved_score (95, 10) == 100

def test_curved_score_negative_bonus():
    with pytest.raises(ValueError):
        curved_score(80, -5)