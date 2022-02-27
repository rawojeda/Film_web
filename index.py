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
        print(cursor)
        mysql.connection.commit()
        '''permite que se creen los mismos usuarios'''
        return redirect(url_for('home'))

@app.route('/Profile')
def profile():
    return render_template('Profile.html')

@app.route('/log_in')
def log_in():
    return render_template('Log_in.html')

@app.route('/enter_user',methods=['POST'])
def enter_user():
    if request.method == 'POST':
        email= request.form['email']
        password=request.form['pass']
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE EMAIL = %s and PASSWORD=%s',(email, password))
        return render_template('Profile.html', user=cursor.fetchall()[0])

@app.route('/delete/<string:userName>')
def delete_user(userName):
    cursor=mysql.connection.cursor()
    cursor.execute('DELETE FROM users WHERE USERNAME = %s',[userName])
    mysql.connection.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:userName>', methods=['POST'])
def edit(userName):
    cursor=mysql.connection.cursor()
    newEmail= request.form['email']
    newPass=request.form['pass']
    if newEmail:
        if newPass:
            cursor.execute('UPDATE users SET EMAIL = %s WHERE USERNAME = %s',(newEmail,userName))
            cursor.execute('UPDATE users SET PASSWORD = %s WHERE USERNAME = %s',(newPass,userName))
            mysql.connection.commit()
        else:
            cursor.execute('UPDATE users SET EMAIL = %s  WHERE USERNAME = %s',(newEmail,userName))
            mysql.connection.commit()
    elif newPass:
        cursor.execute('UPDATE users SET PASSWORD = %s WHERE USERNAME = %s',(newPass,userName))
        mysql.connection.commit()

    cursor2=mysql.connection.cursor()
    cursor2.execute('SELECT * FROM users WHERE USERNAME = %s',[userName])
    return render_template('Profile.html', user=cursor2.fetchall()[0])

def pagina_no_encontrada(error):
    return render_template('NotFound.html')

if __name__ ==  '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True,port=5000)