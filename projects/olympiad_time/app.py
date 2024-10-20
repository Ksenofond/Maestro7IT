from flask import Flask, render_template, redirect, url_for
from models.student import Student
from forms.student_form import StudentForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Mock data for students
students = []

@app.route('/')
def index():
    return render_template('index.html', students=students)

@app.route('/student/<int:student_id>')
def student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    return render_template('student.html', student=student)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form = StudentForm()
    if form.validate_on_submit():
        student_id = len(students) + 1
        new_student = {
            'id': student_id,
            'name': form.name.data,
            'grade': form.grade.data,
            'olympiads': form.olympiads.data.split(',')
        }
        students.append(new_student)
        return redirect(url_for('index'))
    return render_template('add_student.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

