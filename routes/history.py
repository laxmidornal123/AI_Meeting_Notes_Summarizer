from flask import Blueprint, render_template
from flask_login import login_required, current_user
from flask import send_file
import os
from flask import flash, redirect, url_for
from flask_login import login_required, current_user
from models import db
from models.meeting import Meeting
from utils.pdf_generator import generate_pdf
from models.meeting import Meeting

history_bp = Blueprint("history", __name__)


@history_bp.route("/history")
@login_required
def history():

    meetings = Meeting.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Meeting.upload_date.desc()
    ).all()

    return render_template(
        "history.html",
        meetings=meetings
    )


@history_bp.route("/meeting/<int:id>")
@login_required
def meeting(id):

    meeting = Meeting.query.get_or_404(id)
    meetings = Meeting.query.filter_by(
    user_id=current_user.id
).all()
    return render_template(
    "result.html",
    transcript=meeting.transcript,
    summary=meeting.summary,
    meeting=meeting
)
@history_bp.route("/delete/<int:id>")
@login_required
def delete_meeting(id):

    meeting = Meeting.query.get_or_404(id)

    if meeting.user_id != current_user.id:
        flash("Unauthorized access.", "danger")
        return redirect(url_for("history.history"))

    db.session.delete(meeting)
    db.session.commit()

    flash("Meeting deleted successfully.", "success")

    return redirect(url_for("history.history"))

@history_bp.route("/download/<int:id>")
@login_required
def download_report(id):

    meeting = Meeting.query.get_or_404(id)

    os.makedirs("static/reports", exist_ok=True)

    pdf_path = os.path.join(
        "static",
        "reports",
        f"meeting_{meeting.id}.pdf"
    )

    generate_pdf(
        pdf_path,
        meeting.transcript,
        meeting.summary
    )

    return send_file(
        pdf_path,
        as_attachment=True
    )