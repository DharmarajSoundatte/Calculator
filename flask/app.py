# app.py (Flask Application)

from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

def calculator(num1, num2, operation):
    if operation == 'Addition':
        return np.add(num1, num2)
    elif operation == 'Subtraction':
        return np.subtract(num1, num2)
    elif operation == 'Multiplication':
        return np.multiply(num1, num2)
    elif operation == 'Division':
        return np.divide(num1, num2)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        result = calculator(num1, num2, operation)
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
