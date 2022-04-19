from datetime import datetime
from email.policy import default
from pickle import FALSE
from turtle import tilt, title
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno}-> {self.title}"


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == "POST":
        title = (request.form['title'])
        desc = (request.form['desc'])
        todo = Todo(title=title, description=desc)
        db.session.add(todo)
        db.session.commit()
        allTodo = Todo.query.all()
        return render_template('index.html', allTodo=allTodo)

    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)
    # return "<p>Hello, World!</p>"


@app.route("/show")
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return "This is product page"


@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        title = (request.form['title'])
        desc = (request.form['desc'])
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.description = desc
        db.session.add(todo)
        db.session.commit()
        return redirect('/')

    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)


@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
    # To Change the port
    # app.run(debug=True, port=8000)