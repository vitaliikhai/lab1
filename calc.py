from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/plus/<int:a>/<int:b>', methods=['GET'])
def add(a, b):
    result = a + b
    return jsonify({"result": result})

@app.route('/minus/<int:a>/<int:b>', methods=['GET'])
def subtract(a, b):
    result = a - b
    return jsonify({"result": result})

@app.route('/multiply/<int:a>/<int:b>', methods=['GET'])
def multiply(a, b):
    result = a * b
    return jsonify({"result": result})

@app.route('/divide/<int:a>/<int:b>', methods=['GET'])
def divide(a, b):
    if b == 0:
        return jsonify({"error": "Division by zero is not allowed"}), 400
    result = a / b
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)

