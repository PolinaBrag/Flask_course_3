from flask import Flask, render_template
from models import db, Student, Faculty

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


def init_db():
    db.create_all()
    print('OK')


def add_test_data():
    count = 5

    for faculty in range(1, count + 1):
        new_faculty = Faculty(name_fac=f'Факультет{faculty}')
        db.session.add(new_faculty)
    db.session.commit()

    print("Faculty OK")

    for student in range(1, count + 1):
        new_student = Student(name=f'Имя{student}', surname=f'Фамилия{student}',
                              age=f'{student + 15}', gender= f'Муж.', group=f'{student + 1}', faculty_id= f'{student}')
        db.session.add(new_student)
    db.session.commit()

    print("Student OK")


@app.route('/')
def index():
    return 'Hi'


@app.route('/students/')
def all_students():
    all_stud= Student.query.all()
    context = {'students': all_stud}
    return render_template('students.html', **context)


if __name__ == '__main__':
    # with app.app_context():
    #     init_db()
    #     add_test_data()
    app.run()