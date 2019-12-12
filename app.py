from flask import Flask, render_template

app = Flask(__name__)  # create flask application

@app.route('/')
def index():
    who = 'MUMT IT Team'  # variable
    return render_template('index.html', who=who)


@app.route('/greeting/<greeting>')
def greet(greeting):
    return render_template('greet.html', greeting=greeting)


if __name__ == '__main__':
    app.run(debug=True)

