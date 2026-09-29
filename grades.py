# code for grades

def calculate_total(marks):
    total = 0
    for m in marks:
        total = total + m
    return total


def calculate_percentage(marks):
    if len(marks) == 0:
        return 0
    total = calculate_total(marks)
    return round(total / len(marks), 2)


def get_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"