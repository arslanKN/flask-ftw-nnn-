from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/<title>')
@app.route('/index/<title>')
def odd_even(title):
    return render_template('index.html', title=title)
if __name__ == '__main__':
    app.run(port=8090, host='127.0.0.1')