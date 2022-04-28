from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def create_form():
    return render_template("survey.html")


@app.route('/process', methods=['post'])
def process_form():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')


@app.route('/result')
def show_form():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True, port=5007)
