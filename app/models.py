from app import db

class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True, unique=True)
    moduleNum = db.Column(db.String(8))
    deadline = db.Column(db.String(10))
    description = db.Column(db.String(500))
    isDone = db.Column(db.Boolean, default=False) 
