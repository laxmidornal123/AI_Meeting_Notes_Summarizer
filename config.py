import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "change_this_to_a_long_random_secret_key"
    )

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" +
        os.path.join(BASE_DIR, "app.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = os.path.join(
        BASE_DIR,
        "static",
        "uploads"
    )

    REPORT_FOLDER = os.path.join(
        BASE_DIR,
        "static",
        "reports"
    )

    MAX_CONTENT_LENGTH = 200 * 1024 * 1024

    ALLOWED_EXTENSIONS = {
    "mp3",
    "wav",
    "m4a",
    "aac",
    "ogg",
    "flac",
    "wma",
    "mp4",
    "mpeg",
    "mpga",
    "webm",
    "3gp",
    "mov",
    "mkv"
}