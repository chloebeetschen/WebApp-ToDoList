from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class CreateAssessmentForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    moduleNum = StringField('moduleNum', validators=[DataRequired(), Length(max=8)])
    deadline = StringField('deadline', validators=[DataRequired(), Length(max=10)])
    description = TextAreaField('description', validators=[DataRequired()])
    
    submit = SubmitField('Add Record')
