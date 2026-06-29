from transformers import pipeline

summarizer = None


def get_summarizer():
    global summarizer

    if summarizer is None:
        print("Loading AI Summarizer...")

        summarizer = pipeline(
            "summarization",
            model="sshleifer/distilbart-cnn-12-6"
        )

        print("Summarizer Loaded")

    return summarizer


def summarize_text(text):

    if len(text) < 100:
        return text

    model = get_summarizer()

    result = model(
        text,
        max_length=150,
        min_length=40,
        do_sample=False
    )

    return result[0]["summary_text"]