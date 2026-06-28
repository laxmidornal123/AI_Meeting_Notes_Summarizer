from app import app
from models.meeting import Meeting

with app.app_context():
    meetings = Meeting.query.all()

    print("Total Meetings:", len(meetings))

    for meeting in meetings:
        print(meeting.id, meeting.filename)