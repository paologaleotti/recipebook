# tutorial pt 4 19:38
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = '272e5d74fdba4572ea84ab0e570da26a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipeapp.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.png')
    password = db.Column(db.String(60), nullable=False)
    # relazione 1 - N per ricette e autori:
    recipes = db.relationship('Recipe', backref='author', lazy='True')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    prep_time = db.Column(db.String(3), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime(
        120), nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted})"


# DATI PER PROVARE
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
#########


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
            flash(
                f'Login non riuscito, per favore controlla nome utente e password.', 'danger')
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
