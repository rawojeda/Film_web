from flask import Flask, render_template

app= Flask(__name__)


@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/Films')
def films_to_see():
    films=("Avril y el mundo alterado", "Hair high", "kung fu hustle", "Neo tokyo",
           "Redline", "last night in soho", "gozu", "The Congress", "House")
    return render_template('Films.html',peliculas= films)

@app.route('/Contact')
def contacto():
    return render_template('Contact.html')

if __name__ ==  '__main__':
    app.run(debug=True,port=5000)