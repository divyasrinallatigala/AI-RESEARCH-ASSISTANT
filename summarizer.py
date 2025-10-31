from transformers import pipeline

def load_summarizer():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

summarizer = load_summarizer()

def summarize_text(text, max_length=120):
    """Generate concise summary of a research abstract."""
    try:
        result = summarizer(text, max_length=max_length, min_length=30, do_sample=False)
        return result[0]["summary_text"]
    except Exception:
        return text[:300] + "..."  # fallback if text too long


def extract_key_insights(text):
    """Extract 3 main insights or contributions from abstract text."""
    prompt = (
        "Extract three key insights or contributions from the following research abstract:\n\n"
        f"{text}\n\n"
        "Output format:\n1.\n2.\n3."
    )
    try:
        result = summarizer(prompt, max_length=150, min_length=40, do_sample=False)
        insights = result[0]["summary_text"]
        return insights
    except Exception:
        # fallback heuristic: split by sentence
        sentences = text.split('. ')
        top3 = sentences[:3]
        return "\n".join([f"{i+1}. {s}" for i, s in enumerate(top3)])

