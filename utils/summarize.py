from transformers import pipeline

print("Loading AI Summarizer...")

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

print("Summarizer Loaded")


def summarize_text(text):

    if len(text) < 100:
        return text

    result = summarizer(
        text,
        max_length=150,
        min_length=40,
        do_sample=False
    )

    return result[0]["summary_text"]