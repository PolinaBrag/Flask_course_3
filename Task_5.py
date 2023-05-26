from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField, DateField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from flask import Flask, render_template, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=6)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    date_birth = DateField('Date of birth', validators=[DataRequired()])


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        return 'Вы успешно зарегистрировались!'
    return render_template('reg.html', form=form)


if __name__ == '__main__':
    app.run()