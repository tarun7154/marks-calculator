# ptoject test

import grades

def test_total():
    assert grades.calculate_total([80, 70, 90]) == 240

def test_percentage():
    assert grades.calculate_percentage([80, 70, 90]) == 80.0

def test_percentage_empty():
    assert grades.calculate_percentage([]) == 0

def test_grades():
    assert grades.get_grade(95) == "A"
    assert grades.get_grade(80) == "B"
    assert grades.get_grade(65) == "C"
    assert grades.get_grade(45) == "D"
    assert grades.get_grade(20) == "F"

test_total()
test_percentage()
test_percentage_empty()
test_grades()
print("All tests passed.")