# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)



import json
import numpy as np


def open_json_file(json_filename):
    json_file = open(json_filename, encoding='utf-8').read()
    json_data = json.loads(json_file)
    return json_data

def find_student_name_and_surname(students, ident):
    student_name_and_surname = "name surname"
    for student in students:
        if student['ident'] == ident:
            student_name_and_surname = student['name'] + " " + student['surname']
    return student_name_and_surname

def count_student_average_score(school_classes, ident):
    average_scores = []
    for school_class in school_classes:
        if school_class['student_ident'] == ident:
            average_scores.append(np.average(school_class['score']))
    average_score = np.average(average_scores)
    return average_score


if __name__ == "__main__":

    students = open_json_file("students.json")
    school_classes = open_json_file("classes.json")

    print("All students")
    for student in students:
        print("\t", student['name'], student['surname'])

    print()

    print("All school classes")
    class_names = set()
    for school_class in school_classes:
        class_names.add(school_class['name'])
    for class_name in class_names:
        print("\t", class_name)

    print()

    print("Attendance")
    for school_class in school_classes:
        student_name_and_surname = find_student_name_and_surname(students, school_class['student_ident'])
        attendance = np.average(school_class['attendance']) * 100.0
        print("\t", school_class['name'], ": " , student_name_and_surname, " with ", "%.2f"% attendance, "% attendance",sep="")

    print()

    print("Students average score in every class")
    for school_class in school_classes:
        student_name_and_surname = find_student_name_and_surname(students, school_class['student_ident'])
        score = np.average(school_class['score'])
        print("\t", school_class['name'], ": " , student_name_and_surname, " with average score ", "%.1f"% score,sep="")

    print()

    print("Students average score across classes")
    conclusion = "PASSED"
    for student in students:
        score = count_student_average_score(school_classes, student['ident'])
        if score < 3.0:
            conclusion = "FAILED"
        print("\t", student['name'] , student['surname'], "with average score across classes", "%.2f"% score, conclusion)
