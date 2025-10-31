# ui.py
import streamlit as st
from main import fetch_papers
from summarizer import summarize_text, extract_key_insights

st.set_page_config(page_title="AI Research Assistant", layout="wide")
st.title("🧠 AI Research Assistant")
st.write("Enter a topic to get top 5 papers, their summaries, and key insights.")

topic = st.text_input("Enter topic", "artificial intelligence")

if st.button("Fetch & Summarize"):
    with st.spinner("Fetching papers..."):
        papers = fetch_papers(topic)

    st.success(f"Found {len(papers)} papers on '{topic}'.")

    for i, paper in enumerate(papers, start=1):
        st.markdown(f"### {i}. {paper['title']}")
        st.write(f"**Authors:** {', '.join(paper['authors'])}")
        st.write(f"**Published:** {paper['published']}")
        st.write(f"[View on arXiv]({paper['link']})")

        with st.spinner("Summarizing abstract..."):
            summary = summarize_text(paper['summary'])
        st.markdown("**Summary:**")
        st.write(summary)

        with st.spinner("Extracting key insights..."):
            insights = extract_key_insights(paper['summary'])
        st.markdown("**Key Insights / Contributions:**")
        st.write(insights)

        st.markdown("---")
