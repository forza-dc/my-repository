from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is home page for no path, <h1> Welcome Home </h1>'

@app.route('/about')
def about():
    return '<h1> This is my about page </h1>'

@app.route('/error')
def error():
    return '<h1> Either you encountered an error or you are not authorized.</h1>'

@app.route('/admin')
def admin():
    return redirect('/error')

@app.route('/<name>')
def greet(name):
    return f'<h1>Hello, {name}!</h1>'

@app.route('/greet-admin')
def greet_admin():
    return redirect('/John Doe')
    
@app.route('/<name>')
def greet_user(name):
    return render_template('greet.html', name=name)

@app.route('/list10')
def list10():
    numbers = range(1,11)
    return render_template('list10.html', numbers=numbers)

@app.route('/evens')
def evens():
    numbers = range(2,11,2)
    return render_template('evens.html', numbers=numbers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)