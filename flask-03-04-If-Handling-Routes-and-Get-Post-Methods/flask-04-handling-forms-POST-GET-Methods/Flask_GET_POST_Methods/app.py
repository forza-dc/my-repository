from flask import Flask, render_template, request

app = Flask(__name__)

def lcm(a, b):
    greater = max(a, b)

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater = greater + 1
    return lcm

@app.route('/')
def index():
    num1 = 10
    num2 = 20
    return render_template('index.html', num1=num1, num2=num2)

@app.route('/calc', methods=['GET', 'POST'])
def calculate_lcm():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = lcm(num1, num2)
        return render_template('result.html', result=result)
    else:
        return 'Since this is a GET request, LCM has not been calculated'

if __name__ == '__main__':
    app.run(debug=True)
