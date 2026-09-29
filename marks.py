
import os

subjects = ["Maths", "Science", "English"]


def add_student(records):
    name = input("Enter student name: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return

    marks = []
    for sub in subjects:
        # keep asking until a valid number between 0 and 100 is entered
        while True:
            try:
                m = int(input("Enter marks in " + sub + " (0-100): "))
                if m < 0 or m > 100:
                    print("Marks should be between 0 and 100.")
                else:
                    marks.append(m)
                    break
            except ValueError:
                print("Please enter a number.")

    records.append({"name": name, "marks": marks})
    print("Added", name)


def view_students(records):
    if len(records) == 0:
        print("No students yet.")
        return
    for r in records:
        print(r["name"], "=", r["marks"])


def save_records(records, filename="data/marks.txt"):
    f = open(filename, "w")
    for r in records:
        line = r["name"]
        for m in r["marks"]:
            line = line + "," + str(m)
        f.write(line + "\n")
    f.close()
    print("Saved.")


def load_records(filename="data/marks.txt"):
    records = []
    if not os.path.exists(filename):
        return records
    f = open(filename, "r")
    for line in f:
        line = line.strip()
        if line == "":
            continue
        parts = line.split(",")
        marks = []
        for p in parts[1:]:
            marks.append(int(p))
        records.append({"name": parts[0], "marks": marks})
    f.close()
    return records