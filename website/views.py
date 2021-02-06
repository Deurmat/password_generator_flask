from flask import Blueprint, render_template, request, flash
import string
from random import seed, randint

views = Blueprint('views', __name__)

password_list = []


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        password_length = request.form.get('passwordSettingsLength')
        password_numbers = request.form.get('passwordSettingsNumbers') is not None
        password_special = request.form.get('passwordSettingsSpecialChar') is not None
        password_uppercase = request.form.get('passwordSettingsUppercase') is not None
        password_lowercase = request.form.get('passwordSettingsLowercase') is not None

        if password_numbers or password_special or password_uppercase or password_lowercase:
            password_list.append(calculate_password(password_length, password_numbers, password_special, password_uppercase, password_lowercase))
            flash('Password created', category='success')

        else:
            flash('Please tick at least one of the password option boxes', category='error')
    return render_template('home.html', password_list=password_list)


@views.route('/about')
def about():
    return render_template('about.html')


def calculate_password(password_length, include_numbers, include_special, include_upper, include_lower):
    seed()
    char_list = []
    # add numbers
    if include_numbers:
        char_list += [str(x) for x in range(0, 10)]
    if include_special:
        char_list += ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    if include_upper:
        char_list += list(string.ascii_uppercase)
    if include_lower:
        char_list += list(string.ascii_lowercase)
    generated_password_list = [str(char_list[randint(0, len(char_list) - 1)]) for x in range(0, (int(password_length) + 1))]
    return "".join(generated_password_list)
