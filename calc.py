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


@app.route('/calculate', methods=['POST'])

def calculate():
    try:
        # Отримуємо дані з форми
        a = float(request.form['a'])
        b = float(request.form['b'])
        operation = request.form['operation']

        # Виконання операцій
        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            if b != 0:
                result = a / b
            else:
                return render_template('index.html', error="Cannot divide by zero.")

        return render_template('index.html', result=result)
    except ValueError:
        return render_template('index.html', error="Invalid input. Please enter valid numbers.")
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

#         app.run(debug=True)

# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=80)
