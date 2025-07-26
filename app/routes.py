from flask import Blueprint, request, jsonify
from app import db
from app.models import Task

bp = Blueprint("main", __name__)

@bp.route("/health")
def health():
    return jsonify({"status": "ok"})

@bp.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": t.id, "title": t.title, "desc": t.description} for t in tasks])

@bp.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    task = Task(title=data["title"], description=data.get("description", ""))
    db.session.add(task)
    db.session.commit()
    return jsonify({"id": task.id}), 201

from flask import render_template, request, redirect, url_for

@bp.route("/tasks/html", methods=["GET", "POST"])
def tasks_html():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form.get("description", "")
        new_task = Task(title=title, description=description)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("main.tasks_html"))

    tasks = Task.query.all()
    return render_template("tasks.html", tasks=tasks)
