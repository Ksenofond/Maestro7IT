from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class StudentForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    grade = SelectField('Класс', choices=[('10', '10'), ('11', '11')], validators=[DataRequired()])
    olympiads = StringField('Олимпиады (через запятую)', validators=[DataRequired()])
    submit = SubmitField('Добавить ученика')
