from flask import Flask, jsonify, render_template, request
from interfaces.arithmetic import ArithmeticOperation


class Arithmetic(ArithmeticOperation):
    """Реалізація інтерфейсу арифметичних операцій_"""

    def add(self, a: int, b: int) -> int:
        return a + b

    def subtract(self, a: int, b: int) -> int:
        return a - b

    def multiply(self, a: int, b: int) -> int:
        return a * b

    def divide(self, a: int, b: int) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b


app = Flask(__name__)
arithmetic = Arithmetic()

@app.route('/')
def index():
    return render_template('index.html')  # Рендеримо HTML сторінку з формою


app.route('/calculate', methods=['POST'])


def calculate():
    try:
        a = int(request.form['a'])
        b = int(request.form['b'])
        operation = request.form['operation']

        if operation == 'add':
            result = arithmetic.add(a, b)
        elif operation == 'subtract':
            result = arithmetic.subtract(a, b)
        elif operation == 'multiply':
            result = arithmetic.multiply(a, b)
        elif operation == 'divide':
            result = arithmetic.divide(a, b)
        else:
            result = 'Invalid operation'

        return render_template('index.html', result=result)

    except ValueError as e:
        return render_template('index.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True)
