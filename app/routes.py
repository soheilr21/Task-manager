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
