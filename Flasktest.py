from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '你好世界33333!'

@app.route('/hello/')
def hello():
    return 'myworld'


if __name__ == '__main__':
    app.run(debug=True)
