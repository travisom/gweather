from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def search():
    api_key = "2e55387f2ae53ea3f1b86cf7da9d81d9"
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
