import arxiv
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="YOUR_API_KEY")  # Replace with your actual API key

# Fetch papers from arXiv by topic
def fetch_papers(topic, max_results=5):
    search = arxiv.Search(
        query=f'all:"{topic}"',  # search for topic in all fields
        max_results=max_results * 2,  # fetch extra for filtering
        sort_by=arxiv.SortCriterion.Relevance
    )
    papers = []
    for result in search.results():
        papers.append({
            "title": result.title,
            "authors": [a.name for a in result.authors],
            "summary": result.summary,
            "published": result.published.date(),
            "link": result.entry_id
        })
    return papers

# Filter irrelevant papers using GPT
def filter_relevant_papers(papers, topic):
    relevant = []
    for p in papers:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a research assistant that identifies papers directly related to a given topic."},
                {"role": "user", "content": f"Is this paper clearly related to '{topic}'?\n\nTitle: {p['title']}\nAbstract: {p['summary']}\n\nAnswer yes or no."}
            ]
        )
        if "yes" in response.choices[0].message.content.lower():
            relevant.append(p)
        if len(relevant) >= 5:
            break
    return relevant
