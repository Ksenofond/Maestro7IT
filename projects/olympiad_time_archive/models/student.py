class Student:
    def __init__(self, student_id, name, grade, olympiads):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.olympiads = olympiads

from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Student {self.name}, Score {self.score}>'
