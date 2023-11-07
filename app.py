from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


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