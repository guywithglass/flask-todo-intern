from flask import Flask, redirect, render_template, request
from email.policy import default
from pickle import FALSE
from turtle import tilt, title
from models import *


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


@app.route("/registration")
def registration():
    return render_template('registration.html')


if __name__ == "__main__":
    app.run(debug=True)
    # To Change the port
    # app.run(debug=True, port=8000)
