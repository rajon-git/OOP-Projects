from person import Teacher

class Subject:
    def __init__(self,name,teacher):
        self.name=name
        self.teacher=teacher
        self.max_marks = 100
        self.pass_marks = 33

    def exam(self,students):
        for student in students:
            mark = self.teacher.evaluate_exam()
