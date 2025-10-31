import arxiv

def fetch_papers(topic, max_results=5):
    search = arxiv.Search(
        query=topic,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    papers = []
    for result in search.results():
        papers.append({
            "title": result.title,
            "authors": [a.name for a in result.authors],
            "summary": result.summary.replace("\n", " "),
            "published": result.published.date(),
            "link": result.entry_id
        })
    return papers
