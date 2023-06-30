from flask import Flask, render_template, request
from wtforms import Form, StringField, PasswordField, validators

app = Flask(__name__)

class RegistrationForm(Form):
    username = StringField('Ім\'я користувача', [validators.Length(min=4, max=25)])
    email = StringField('Email адреса', [validators.Email()])
    password = PasswordField('Пароль', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Паролі повинні збігатися')
    ])
    confirm = PasswordField('Підтвердити пароль')
    age = StringField('Вік', [validators.Optional()])

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # Отримати дані з форми
        username = form.username.data
        email = form.email.data
        password = form.password.data
        age = form.age.data

        # Виконати логіку реєстрації користувача

        return 'Реєстрація пройшла успішно!'
    return render_template('registration.html', form=form)

if __name__ == '__main__':
    app.run()
