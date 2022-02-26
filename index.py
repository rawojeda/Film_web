from flask import Flask, render_template, url_for, redirect, request, flash
from flask_mysqldb import MySQL

app= Flask(__name__)

data_base= MySQL();
app.config['MYSQL_HOST'] = 'localhost';
app.config['MYSQL_USER'] = 'root';
app.config['MYSQL_PASSWORD'] = '';
app.config['MYSQL_DB'] = 'films';
mysql= MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/')
def home():
    return render_template('Index.html')




@app.route('/Reviews')
def reviews():
    return render_template('Reviews.html')




@app.route('/Top_films')
def Top_films():
    return render_template('Top_films.html')

@app.route('/Films_to_see')
def films_to_see():
    films=("Avril y el mundo alterado", "Hair high", "kung fu hustle", "Neo tokyo",
           "Redline", "last night in soho", "gozu", "The Congress", "House")
    return render_template('Films_to_see.html',peliculas= films)

@app.route('/suggestions')
def suggestions():
    return render_template('suggestions.html')

@app.route('/sign_in')
def sign_in():
    return render_template('Sign_in.html')

@app.route('/add_user',methods=['POST'])
def add_user():
    if request.method == 'POST':
        userName = request.form['userName']
        email= request.form['email']
        password=request.form['pass']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users (USERNAME, EMAIL, PASSWORD) VALUES (%s, %s, %s)', (userName, email, password))
        mysql.connection.commit()
        flash("Contact added successfully")
        '''permite que se creen los mismos usuarios'''
        return redirect(url_for('home'))



'''
@app.route('/film',methods=['POST'])
def film:
    data={
        'name': nombre,
        'Director': "Martin Escorsese",
        'Year': 1990
    }
    return render_template('film.html', film_data=data)

@app.route('/film/<nombre>')
def film(nombre):
    data={
        'name': nombre,
        'Director': "Martin Escorsese",
        'Year': 1990
    }
    return render_template('film.html', film_data=data)
'''
def pagina_no_encontrada(error):
    return render_template('NotFound.html')
    #return redirect(url_for('home'))

if __name__ ==  '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True,port=5000)