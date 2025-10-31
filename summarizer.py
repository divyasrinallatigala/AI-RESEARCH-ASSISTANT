from transformers import pipeline

def load_summarizer():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

summarizer = load_summarizer()

def summarize_text(text, max_len=150):
    summary = summarizer(text, max_length=max_len, min_length=50, do_sample=False)
    return summary[0]['summary_text']

def extract_key_insights(text):
    insights = summarizer(text, max_length=80, min_length=30, do_sample=False)
    return insights[0]['summary_text']
