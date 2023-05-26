from flask import Flask, render_template
from models_2 import db, Book, Author

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_2.db'
db.init_app(app)


def init_db():
    db.create_all()
    print('OK')


def add_test_data():
    count = 3

    for author in range(1, count + 1):
        new_author = Author(name=f'Имя{author}', surname=f'Фамилия{author}')
        db.session.add(new_author)
    db.session.commit()

    print("Author OK")

    for book in range(1, count + 1):
        new_book = Book(name=f'Название{book}', year=f'{1950 + book}',
                              count_books=f'{book + 10}', author_id= f'{book}')
        db.session.add(new_book)
    db.session.commit()

    print("Book OK")


@app.route('/')
def index():
    return 'Hi'


@app.route('/books/')
def books():
    all_books= Book.query.all()
    context = {'books': all_books}
    return render_template('books.html', **context)


if __name__ == '__main__':
    # with app.app_context():
    #     init_db()
    #     add_test_data()
    app.run()