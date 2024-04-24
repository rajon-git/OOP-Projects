class Classroom:
    def __init__(self,name):
        self.name=name
        self.students =[]
        self.subjects =[]

    def add_student(self,student):
        roll_no = f"{self.name} - {len(self.students)+1}" #eight-1
        student.id = roll_no
        self.students.append(student)
    def add_subjcet(self,subject):
        self.subjects.append(subject)