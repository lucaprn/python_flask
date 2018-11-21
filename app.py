from flask import Flask, request, redirect, make_response, abort


app = Flask(__name__)

# pagina principale del sito

@app.route('/')
def hello_world():
    return 'Ciao'

@app.route('/user/<name>')
def user(name):
    return '<h1> Hello %s </h1>' % name

# pagina secondaria autogenerata

@app.route('/prova')
def prova():
    return 'Prova'

# request

@app.route('/request')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

# reindirizza

@app.route('/reindirizza')
def reindirizza():
    return redirect('https://www.google.it')

if __name__ == '__main__':
    app.run()
