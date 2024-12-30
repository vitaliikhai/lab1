from flask import Flask, jsonify
from interfaces.arithmetic import ArithmeticOperation


class Arithmetic(ArithmeticOperation):
    """Реалізація інтерфейсу арифметичних операцій"""

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

@app.route('/plus/<int:a>/<int:b>', methods=['GET'])
def add(a, b):
    result = arithmetic.add(a, b)
    return jsonify({"result": result})

@app.route('/minus/<int:a>/<int:b>', methods=['GET'])
def subtract(a, b):
    result = arithmetic.subtract(a, b)
    return jsonify({"result": result})

@app.route('/multiply/<int:a>/<int:b>', methods=['GET'])
def multiply(a, b):
    result = arithmetic.multiply(a, b)
    return jsonify({"result": result})

@app.route('/divide/<int:a>/<int:b>', methods=['GET'])
def divide(a, b):
    try:
        result = arithmetic.divide(a, b)
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
