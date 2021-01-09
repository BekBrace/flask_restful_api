from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'GET'):
        data = "Happy New Year 2021"
        return jsonify({'A message': data})


@app.route('/<int:num>', methods=['GET'])
def cube(num):
    return jsonify({f'Cube number of {num}': num**3})


if __name__ == "__main__":
    app.run(debug=True)
