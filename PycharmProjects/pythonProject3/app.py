from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>hellow mogadisho</h1>'


@app.route('/home', methods=['GET' ,'POST'], defaults={'name': 'Default'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    return '<h1>hellow {},you are mog</h1>'.format(name)

@app.route('/json')
def json():
    return jsonify({'key': 'value', 'key2': [1, 2, 3, 3]})


if __name__ == "__main__":
    app.run()
