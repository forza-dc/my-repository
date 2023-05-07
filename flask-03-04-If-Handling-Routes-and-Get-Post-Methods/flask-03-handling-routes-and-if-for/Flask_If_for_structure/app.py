from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', message="This is my first conditions experience")

@app.route('/header')
def header():
    elements = [1, 2, 3, 4, 5]
    return render_template('index.html', elements=elements)

if __name__ == '__main__':
    app.run(debug=True)
