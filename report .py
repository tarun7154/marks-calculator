# code for report card and check topper and class average 

import grades


def show_report(records):
    if len(records) == 0:
        print("No students yet.")
        return
    print("\nName\tTotal\tPercent\tGrade")
    print("--------------------------------")
    for r in records:
        total = grades.calculate_total(r["marks"])
        percent = grades.calculate_percentage(r["marks"])
        grade = grades.get_grade(percent)
        print(r["name"], "\t", total, "\t", percent, "\t", grade)


def find_topper(records):
    if len(records) == 0:
        print("No students yet.")
        return
    best = records[0]
    for r in records:
        if grades.calculate_total(r["marks"]) > grades.calculate_total(best["marks"]):
            best = r
    print("Topper is", best["name"], "with total", grades.calculate_total(best["marks"]))


def class_average(records):
    if len(records) == 0:
        print("No students yet.")
        return
    total_percent = 0
    for r in records:
        total_percent = total_percent + grades.calculate_percentage(r["marks"])
    print("Class average:", round(total_percent / len(records), 2), "%")