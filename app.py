import flask
from flask import Flask, render_template, request


app = Flask(__name__, template_folder='C:\\Users\\a3ter\Downloads\\hello_world\\hello_world\\hello_world')

@app.route('/')
def index():
    text = 'Hello, World!'
    return render_template('hello_world_index.html')


if __name__ == '__main__':
    app.run(debug=True)


