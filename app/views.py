from flask import render_template, flash, request
from app import app, db, models
from .forms import CreateAssessmentForm
import datetime


@app.route('/uncompleted_assessments', methods=['GET', 'POST'])
def uncompletedAssessments():
     assessments =  models.Assessment.query.filter_by(isDone=False).all()
     return render_template('uncompleted_assessments.html',
                           title='Uncomplete Assessments',
                           assessments=assessments)



@app.route('/complete/<int:id>', methods=['GET', 'POST'])
def complete(id):
    updated = models.Assessment.query.get(id)
    updated.isDone = True
    db.session.commit()
    assessments =  models.Assessment.query.filter_by(isDone=False).all()
    return render_template('uncompleted_assessments.html',
                           title='Uncomplete Assessments',
                           assessments=assessments)
    

@app.route('/completed_assessments', methods=['GET', 'POST'])
def completedAssessments():
     assessments =  models.Assessment.query.filter_by(isDone=True).all()
     return render_template('completed_assessments.html',
                           title='Complete Assessments',
                           assessments=assessments)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    toDelete = models.Assessment.query.get(id)
    db.session.delete(toDelete)
    db.session.commit()
    assessments =  models.Assessment.query.filter_by(isDone=True).all()
    return render_template('completed_assessments.html',
                           title='complete Assessments',
                           assessments=assessments)


@app.route('/create_assessment', methods=['GET', 'POST'])
def createAssessment():
    form = CreateAssessmentForm()
    if form.validate_on_submit():
        flash('Succesfully created a new assessment!')
        tit = request.form['title']
        num = request.form['moduleNum']
        date = request.form['deadline']
        desc = request.form['description']

        record = models.Assessment(title=tit,
                moduleNum=num, 
                deadline=date, 
                description=desc,
                isDone=False)
        db.session.add(record)
        db.session.commit()

    return render_template('create_assessment.html',
                           title='Create Assessment',
                           form=form)


@app.route('/', methods=['GET', 'POST'])
def home():
    assessments =  models.Assessment.query.all()
    return render_template('all_assessments.html',
                           title='All Assessments',
                           assessments=assessments)
