import pytest
from gradebook import letter_grade, is_passing, average

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

def test_is_passing_true():
    assert is_passing(75) == True 

def test_is_passing_false():
    assert is_passing(45) == False

def test_is_passing_invalid_type():
    with pytest.raises(TypeError):
        is_passing("passing")

def test_average_works():
    assert average([80, 90, 70])