from faster_whisper import WhisperModel
import os

print("Loading Whisper Model...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Model Loaded")


def transcribe_audio(audio_path):

    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"{audio_path} not found")

    segments, info = model.transcribe(
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
        print(f"[{segment.start:.2f}-{segment.end:.2f}] {segment.text}")
        transcript.append(segment.text)

    return " ".join(transcript)