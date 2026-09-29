# Problem Statement & Scope

## Problem Statement
Manual tracking and calculation of student marks, total scores, percentages, letter grades, class averages, and top performers is inefficient and subject to human error. There is a need for an automated, lightweight, modular Python application to simplify grade management, calculate accurate performance metrics, and store records persistently.

## Scope of the Project
This project delivers a modular Python system featuring a console menu driver (`main.ipynb`) that enables educators to manage student mark lists, automatically assign letter grades based on percentage thresholds, generate clean tabular report cards, find class toppers, and save/load records to local disk (`data/marks.txt`).

## Target Users
* School and College Instructors
* Academic Tutors
* Course Coordinators and Teaching Assistants

## High-Level Features
1. **Student Registration:** Add new student records with input validation ensuring marks fall within the 0–100 range.
2. **Record Inspection:** Display registered students along with their individual subject marks.
3. **Report Card Generation:** Compute total marks, percentage, and assign letter grades (A, B, C, D, F).
4. **Topper Identification:** Identify and display the student with the highest total marks across the class.
5. **Class Analytics:** Calculate the overall class percentage average.
6. **Data Persistence:** Automatically save and load records from a local text storage file (`data/marks.txt`).
