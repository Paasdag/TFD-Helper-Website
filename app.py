from flask import Flask, render_template, request, jsonify, abort, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()

# Development variable is used to run the server locally, turn off to make it run on vercel.
development = False
app = Flask(__name__)

SECRET_KEY = os.environ.get("secret_key")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("database_string")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Metric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    total_servers = db.Column(db.Integer, nullable=False)
    total_users = db.Column(db.Integer, nullable=False)
    latency_ms = db.Column(db.Integer, nullable=True)

@app.route("/")
def index_page():
    latest = Metric.query.get(1)
    return render_template("index.html", metrics=latest)

@app.route("/commands")
def commands_page():
    commands = [
    {"cmd": "/info", "desc": "Gets the user's current Descendant, Platform, Mastery."},
    {"cmd": "/reactorinformation", "desc": "Gets the user's equiped reactor and substats."},
    {"cmd": "/descendantmodules", "desc": "Gets all the equiped modules of the user's current equiped descendant"},
    {"cmd": "/componentinfo", "desc": "Gets the component information from the user"},
    {"cmd": "/descendantinfo", "desc": "Gets all information related to the user's current equiped descendant"},
    {"cmd": "/weapons", "desc": "Returns an paginated embed with the users weapon level, modules, cores and stats"},
    ]
    return render_template("commands.html", commands=commands)

@app.route("/api/data", methods=["POST"])
def receive_metrics():
    auth_header = request.headers.get("Authorization", "")
    if auth_header != f"Bearer {SECRET_KEY}":
        abort(401)

    data = request.get_json(force=True)
    total_servers = data.get("total_servers")
    total_users = data.get("total_users")
    latency_ms = data.get("latency_ms")

    if total_servers is None or total_users is None:
        abort(400)

    metric = Metric.query.get(1)
    if not metric:
        metric = Metric(id=1)

    metric.total_servers = total_servers
    metric.total_users = total_users
    metric.latency_ms = latency_ms
    metric.timestamp = datetime.utcnow()

    db.session.add(metric)
    db.session.commit()

    return jsonify({"status": "updated"}), 200

@app.route("/dashboard")
def user_profile():
    latest = Metric.query.get(1)
    return render_template('dashboard.html', metrics=latest)

@app.route("/calc/catalyst")
def catalystcalc():
    return render_template("/calc/catalyst.html")

@app.route("/calc/energy_activator")
def energy_activator_calc():
    return render_template("/calc/energy_activator.html")

@app.route("/calc")
def calc_index():
    return render_template("/calc/calc_index.html")

with app.app_context():
    db.create_all()
    
if development == True:
    if __name__ == "__main__":
        app.run(debug=True)