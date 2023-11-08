from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


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


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_title = db.Column(db.String(50), nullable=False)
    task_text = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow())
    difficulty = db.Column(db.Float, default=1.0)

    def __repr__(self):
        return '<Tasks %r>' % self.id % self.task_title


class Someinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer)
    happyness_level = db.Column(db.Integer, nullable=False)
    has_car = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Someinfo %r>' % self.id


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.id).all()
    return render_template('posts.html', articles=articles)


@app.route('/posts/<int:id>')
def post_details(id):
    article = Article.query.get(id)
    return render_template('post_details.html', article=article)


@app.route('/posts/<int:id>/<string:action>', methods=['POST', 'GET'])
def post_action(id, action):
    article = Article.query.get_or_404(id)
    if action == 'delete':
        try:
            db.session.delete(article)
            db.session.commit()
            return redirect('/posts')
        except:
            return "При удалении статьи произошла ошибка!"
    elif action == 'update':
        if request.method == 'POST':
            article.title = request.form['title']
            article.intro = request.form['intro']
            article.text = request.form['text']

            try:
                db.session.commit()
                return redirect('/posts')
            except:
                return "При редактировании статьи произошла ошибка!"
        else:
            return render_template('post_update.html', article=article)


@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')
        except:
            return "При добавлении статьи произошла ошибка!"
    else:
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
    with app.app_context():
        db.create_all()
    app.run(debug=True)