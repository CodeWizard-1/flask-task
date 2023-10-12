from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task
app.app_context().push()

# Теперь вы находитесь в контексте приложения и можете выполнить операции, требующие доступа к приложению
db.create_all()

@app.route("/")
def home():
    return render_template("base.html")
