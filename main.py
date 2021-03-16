from flask import Flask, render_template, url_for
app = Flask(__name__)

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


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
