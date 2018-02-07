from flask import Flask, render_template, request,url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/visethsen/Desktop/health_check/blog2.db'

db = SQLAlchemy(app)

# class Blogpost(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(50))
#     subtitle = db.Column(db.String(50))
#     author = db.Column(db.String(20))
#     date_posted = db.Column(db.DateTime)
#     content = db.Column(db.Text)

class Blogpost2(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    bloodsugar=db.Column(db.String(50))
    bloodpressure=db.Column(db.String(50))
    author=db.Column(db.String(20))
    date_posted=db.Column(db.DateTime)
    comments=db.Column(db.Text)

@app.route('/')
def index():
    posts = Blogpost2.query.order_by(Blogpost2.date_posted.desc()).all()

    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost2.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/addpost', methods=['POST'])
def addpost():
    bloodpressure=request.form['bloodpressure']
    bloodsugar=request.form['bloodsugar']
    author=request.form['author']
    comments=request.form['comments']

    post = Blogpost2(bloodsugar=bloodsugar, bloodpressure=bloodpressure, author=author, comments=comments, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
