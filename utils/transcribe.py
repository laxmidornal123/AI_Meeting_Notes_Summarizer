from faster_whisper import WhisperModel
import os

model = None


def get_model():
    global model

    if model is None:

        print("Loading Whisper Model...")

        model = WhisperModel(
            "tiny",
            device="cpu",
            compute_type="int8"
        )

        print("Model Loaded")

    return model


def transcribe_audio(audio_path):

    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"{audio_path} not found")

    whisper_model = get_model()

    segments, info = whisper_model.transcribe(
        audio_path,
        beam_size=5,
        vad_filter=False
    )

    transcript = []

    print("=" * 60)
    print("Detected Language :", info.language)
    print("Probability :", info.language_probability)
    print("=" * 60)

    for segment in segments:
        transcript.append(segment.text)

    return " ".join(transcript)