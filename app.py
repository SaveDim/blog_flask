from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Article %r>' % self.id



@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create-article')
def create_article():
    return render_template('create-article.html')

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'User page: ' + name + ' - ' + str(id)


@app.route('/blog/news')
def news():
    return "Some data"

@app.route('/blog/<int:id>/news')
def news_id():
    return "Some data"


@app.route('/admin-<string:login>/<int:id>')
def admin_login(login, id):
    return "Some data"


@app.route('/user/<string:login>')
def user_login(login):
    return render_template('user.html', login=login)


@app.route('/contacti')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)