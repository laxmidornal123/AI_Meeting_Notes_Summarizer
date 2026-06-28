from flask import Blueprint, render_template
from flask_login import login_required, current_user

from models.meeting import Meeting

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/profile")
@login_required
def profile():

    meetings = Meeting.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template(
        "profile.html",
        total_meetings=len(meetings)
    )