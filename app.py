from flask import Flask, request, redirect, render_template



app = Flask(__name__)



# pagina principale del sito

@app.route('/')
def hello_world():
    return render_template('index.html')

# provo ad aprire una pagina creata
@app.route("/prova")
def prova():
    return render_template('prova.html', title='Prova')

@app.route('/user/<name>')
def user(name):
    return '<h1> Hello %s </h1>' % name

# request
@app.route('/request')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

# reindirizza

@app.route('/reindirizza')
def reindirizza():
    return redirect('https://www.google.it')

# intercettazione errori

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
