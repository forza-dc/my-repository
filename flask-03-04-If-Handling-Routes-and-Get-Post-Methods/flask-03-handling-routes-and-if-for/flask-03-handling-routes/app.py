#Import Flask modules

#Create an object named app 


# Create a function named home which returns a string 'This is home page for no path, <h1> Welcome Home</h1>' 
# and assign route of no path ('/')


# Create a function named about which returns a formatted string '<h1>This is my about page </h1>' 
# and assign to the static route of ('about')


# Create a function named error which returns a formatted string '<h1>Either you encountered an error or you are not authorized.</h1>' 
# and assign to the static route of ('error')


# Create a function named admin which redirect the request to the error path 
# and assign to the route of ('/admin')


# Create a function named greet which return formatted inline html string 
# and assign to the dynamic route of ('/<name>')


# Create a function named greet_admin which redirect the request to the hello path with param of 'Master Admin!!!!' 
# and assign to the route of ('/greet-admin')


# Rewrite a function named greet which uses template file named `greet.html` under `templates` folder 
# and assign to the dynamic route of ('/<name>'). 
# Please find a template html file named `greet.html` which takes `name` as parameter under `templates` folder 


# Create a function named list10 which creates a list counting from 1 to 10 within `list10.html` 
# and assign to the route of ('/list10'). 
# Please find a template html file named `list10.html` which shows a list counting from 1 to 10 under `templates` folder 


# Create a function named evens which show the even numbers from 1 to 10 within `evens.html` 
# and assign to the route of ('/evens'). 
# Please find a template html file named `evens.html` which shows a list of even numbers from 1 to 10 under `templates` folder 


# Add a statement to run the Flask application which can be reached from any host on port 80.



from flask import Flask, render_template, redirect, url_for

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
    return redirect(url_for('error'))

@app.route('/name/<string:input_name>')
def greet(input_name):
    return render_template('greet.html', name=input_name)

@app.route('/greet-admin')
def greet_admin():
    return redirect(url_for('greet', input_name='Master Admin!!!'))

@app.route('/list10')
def list10():
    return render_template('list10.html')

@app.route('/evens')
def evens():
    return render_template('evens.html')




if __name__ == '__main__':
    app.run(debug=False, port=80)



# @app.route('/<name>')
# def greet(name):
#     return f'<h1>Hello, {name}!</h1>'

# @app.route('/greet-admin')
# def greet_admin():
#     return redirect('/John Doe')
    
# @app.route('/<name>')
# def greet_user(name):
#     return render_template('greet.html', name=name)

# @app.route('/list10')
# def list10():
#     numbers = range(1,11)
#     return render_template('list10.html', numbers=numbers)

# @app.route('/evens')
# def evens():
#     numbers = range(2,11,2)
#     return render_template('evens.html', numbers=numbers)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=80)