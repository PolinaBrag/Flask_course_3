from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_fac = db.Column(db.String(80), nullable=False)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    surname = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    group = db.Column(db.String(20), nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)
    faculties = db.relationship('Faculty', backref='Student')

    def __repr__(self):
        return f'User({self.name}, {self.surname})'


