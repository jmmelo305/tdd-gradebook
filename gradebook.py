def letter_grade (score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score Must be a number")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def is_passing (score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score Must be a number")
    return score >= 60 

def average (scores):
    return round(sum(scores) / len(scores), 2)

def curved_score(score, bonus):
    pass

