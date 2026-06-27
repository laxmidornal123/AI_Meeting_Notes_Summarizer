from datetime import datetime
from models import db


class Meeting(db.Model):

    __tablename__ = "meetings"

    id = db.Column(db.Integer, primary_key=True)

    filename = db.Column(db.String(255), nullable=False)

    transcript = db.Column(db.Text, nullable=False)

    summary = db.Column(db.Text, nullable=False)

    upload_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )