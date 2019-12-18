from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)  # create flask application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)
migration = Migrate(app, db)
admin = Admin(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer(), primary_key=True, auto_increment=True)
    email = db.Column('email', db.String(), nullable=False)
    firstname = db.Column('firstname', db.String(), nullable=True)
    lastname = db.Column('lastname', db.String(), nullable=True)


admin.add_view(ModelView(User, db.session))


@app.route('/')
def index():
    who = 'MUMT IT Team'  # variable
    return render_template('index.html', who=who)


@app.route('/greeting/<greeting>')
def greet(greeting):
    return render_template('greet.html', greeting=greeting)


if __name__ == '__main__':
    app.run(debug=True)

