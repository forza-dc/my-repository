from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

def greet():
    user = request.args.get('user')
    if user:
        return render_template('greet.html', user=user)
    else:
        return "Please provide a user parameter in the URL."
    
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            return redirect(url_for('secure'))
        else:
            return render_template('login.html', message='Invalid username or password.')
    else:
        return render_template('login.html')
    
@app.route('/secure')
def secure():
    return render_template('secure.html')

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
