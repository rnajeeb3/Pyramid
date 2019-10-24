from flask import Flask, request, render_template, redirect, url_for, json
from checkword import check_word
app = Flask(__name__)


@app.route('/')
def start():
    return render_template("form.html")


@app.route('/', methods=['POST'])
def input_data():
    input_text = request.form['Word']
    result = check_word(input_text)

    return render_template('result.html', name=result)


if __name__ == '__main__':
    app.debug = True
    app.run()
