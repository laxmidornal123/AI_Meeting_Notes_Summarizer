from flask import Blueprint, render_template, request, current_app, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os

from models import db
from models.meeting import Meeting

from utils.transcribe import transcribe_audio
from utils.summarize import summarize_text

upload_bp = Blueprint("upload", __name__)


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in current_app.config["ALLOWED_EXTENSIONS"]
    )


@upload_bp.route("/upload", methods=["GET", "POST"])
@login_required
def upload():

    if request.method == "POST":

        if "audio" not in request.files:
            flash("Please select an audio file.", "warning")

            return render_template("upload.html")

        file = request.files["audio"]

        if file.filename == "":
            flash("No file selected.", "warning")

            return render_template("upload.html")

        if not allowed_file(file.filename):
            flash("Unsupported file format.", "danger")
            return render_template("upload.html")

        filename = secure_filename(file.filename)

        filepath = os.path.join(
            current_app.config["UPLOAD_FOLDER"],
            filename
        )

        os.makedirs(
            current_app.config["UPLOAD_FOLDER"],
            exist_ok=True
        )

        file.save(filepath)

        transcript = transcribe_audio(filepath)

        summary = summarize_text(transcript)

        meeting = Meeting(
            filename=filename,
            transcript=transcript,
            summary=summary,
            user_id=current_user.id
        )

        db.session.add(meeting)
        db.session.commit()

        return render_template(
            "result.html",
            transcript=transcript,
            summary=summary,
            meeting=meeting
        )

    return render_template("upload.html")