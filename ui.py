import streamlit as st
from main import fetch_papers, filter_relevant_papers
from summarizer import summarize_text, extract_key_insights

st.set_page_config(page_title="AI Research Assistant", page_icon="🤖", layout="wide")

st.title("🤖 AI-Powered Research Assistant")
st.markdown("Fetch, summarize, and analyze research papers with AI.")

topic = st.text_input("Enter a research topic:", placeholder="e.g. Quantum computing, LLM alignment, Medical AI")

if st.button("Search Papers"):
    if topic.strip():
        with st.spinner("Fetching relevant papers..."):
            papers = fetch_papers(topic)
            relevant_papers = filter_relevant_papers(papers, topic)

            if not relevant_papers:
                st.warning("No relevant papers found. Try a different or more specific topic.")
            else:
                for i, paper in enumerate(relevant_papers, 1):
                    st.subheader(f"📄 {i}. {paper['title']}")
                    st.write(f"**Authors:** {', '.join(paper['authors'])}")
                    st.write(f"**Published:** {paper['published']}")
                    st.markdown(f"[Read full paper ↗️]({paper['link']})")

                    if st.button(f"Summarize {i}"):
                        with st.spinner("Summarizing..."):
                            summary = summarize_text(paper["summary"])
                            insights = extract_key_insights(paper["summary"])
                            st.success("✅ Summary")
                            st.write(summary)
                            st.info("💡 Key Insights")
                            st.write(insights)
    else:
        st.warning("Please enter a topic to begin.")
