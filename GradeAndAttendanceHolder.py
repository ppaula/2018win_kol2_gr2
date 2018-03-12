class GradeAndAttendanceHolder(object):

	class_id = 0
	student_id = 0

	grades = list()
	attendances = list()


	def __init__(self, class_id, student_id):
		self.class_id = class_id
		self.student_id = student_id

	def set_grade(self, grade):
		self.grades.append(grade)

	def set_attendance(self, attendance):
		self.attendances.append(attendance)

	def get_average_score_in_class(self):
		return sum(self.grades)/len(self.grades)

	def get_attendance(self):
		for a in self.attendances:
			if a == True:
				print(" | Present | ")
			else:
				print (" | Absent  | ")