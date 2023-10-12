from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task
app.app_context().push()


db.create_all()

@app.route("/")
def home():
    return render_template("tasks.html")
