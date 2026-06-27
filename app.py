from flask import Flask, redirect, url_for, render_template
from routes.profile import profile_bp
from config import Config

from models import db, login_manager
from flask_login import current_user, login_required
from models.user import User
from models.meeting import Meeting
from routes.settings import settings_bp
from routes.auth import auth_bp
from routes.upload import upload_bp
from routes.history import history_bp
from flask import Blueprint, render_template
from flask_login import login_required
from routes.reports import reports_bp
app = Flask(__name__)

app.config.from_object(Config)

# Initialize Extensions
db.init_app(app)
login_manager.init_app(app)
settings_bp = Blueprint("settings", __name__)

@settings_bp.route("/settings")
@login_required
def settings():
    return render_template("settings.html")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(history_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(reports_bp)
app.register_blueprint(settings_bp)

with app.app_context():
    db.create_all()


@app.route("/")
def home():

    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    return redirect(url_for("auth.login"))


@app.route("/dashboard")
@login_required
def dashboard():

    meetings = Meeting.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Meeting.upload_date.desc()
    ).all()

    total_meetings = len(meetings)

    return render_template(
        "dashboard.html",
        meetings=meetings,
        total_meetings=total_meetings
    )

if __name__ == "__main__":
    app.run(debug=True)