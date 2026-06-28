from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models.meeting import Meeting

reports_bp = Blueprint("reports", __name__)

@reports_bp.route("/reports")
@login_required
def reports():

    reports = Meeting.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Meeting.upload_date.desc()
    ).all()

    return render_template(
        "reports.html",
        reports=reports
    )