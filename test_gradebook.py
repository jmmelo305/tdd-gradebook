from gradebook import letter_grade

def test_letter_grade_A ():
    assert letter_grade(95) == "A"

def test_letter_grade_F():
    assert letter_grade(45) == "F"

