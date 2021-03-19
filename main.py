from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '272e5d74fdba4572ea84ab0e570da26a'

recipes = [
    {
        'author': 'Paolo Galeotti',
        'title': 'Pasta alla carbonara',
        'prep_time': '25',
        'content': 'Metti la pasta nella carbonara, fatto.',
        'date_posted': 'March 16, 2021'
    },
    {
        'author': 'Mattia Covato',
        'title': 'Jappo time',
        'prep_time': '30',
        'content': 'metti il sushi nel piatto, mhh che buono non è vero evviva la pizza.',
        'date_posted': 'March 13, 2021'
    },
    {
        'author': 'Filippo Bertozzi',
        'title': 'Carbotricana',
        'prep_time': '23',
        'content': 'Carbonara + Amatriciana = Bertozzi.',
        'date_posted': 'March 16, 2021'
    }
]


@app.route('/')
def home():
    return render_template('home.html', recipes=recipes)


@app.route('/recipe')
def recipe():
    return render_template('recipe.html', recipes=recipes)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # dati a caso per prova ----------
        if form.username.data == 'pollo' and form.password.data == 'pass': 
            flash(f'Login eseguito come {form.username.data}!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login non riuscito, per favore controlla nome utente e password.', 'danger')
        # dati a caso per prova ------------
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account creato per {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
