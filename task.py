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

from Student import Student
from Score import Score
from SchoolClass import SchoolClass
from GradeAndAttendanceHolder import GradeAndAttendanceHolder

stud1 = Student("Jan", "Nowak", 1);
stud2 = Student("Ola", "Nowakowska", 2);

school_class1 = SchoolClass("Maths", 1);
school_class1 = SchoolClass("English", 2);

holder1 = GradeAndAttendanceHolder(1, 1)
holder2 = GradeAndAttendanceHolder(1, 2)
holder3 = GradeAndAttendanceHolder(2, 1)
holder4 = GradeAndAttendanceHolder(2, 2)

holder1.set_grade(2)
holder1.set_grade(5)
holder2.set_grade(3)
holder2.set_grade(4)

holder1.set_attendance(True)
holder1.set_attendance(True)
holder3.set_attendance(True)
holder4.set_attendance(False)


print("Average of", stud1.name, stud1.surname, "in", school_class1.name, "is", holder1.get_average_score_in_class())
print("Attendance:")
holder1.get_attendance()
