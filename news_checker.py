# news_checker.py

import requests
from bs4 import BeautifulSoup
import torch
import spacy
from sentence_transformers import SentenceTransformer, util

# Load models
nlp = spacy.load('en_core_web_sm')
sbert = SentenceTransformer('all-MiniLM-L6-v2')

# Fetch article titles and links from Google News RSS
def fetch_google_headlines(query, max_results=10):
    url = f"https://news.google.com/rss/search?q={query}"
    try:
        resp = requests.get(url, timeout=5)
        soup = BeautifulSoup(resp.content, 'xml')
        items = soup.find_all("item")[:max_results]
        return [
            {
                "title": item.title.text,
                "url": item.link.text
            } for item in items
        ]
    except Exception as e:
        return []

# Compute semantic similarity
def compute_similarity(headline, articles):
    if not articles:
        return 0.0, {}
    titles = [a['title'] for a in articles]
    h_emb = sbert.encode([headline], convert_to_tensor=True)
    t_embs = sbert.encode(titles, convert_to_tensor=True)
    sims = util.cos_sim(h_emb, t_embs)[0]
    best_idx = int(torch.argmax(sims))
    best_score = float(sims[best_idx])
    return round(best_score, 2), articles[best_idx]

# Extract SVO using spaCy
def extract_svo(text):
    doc = nlp(text)
    subj, verb, obj = None, None, None
    for token in doc:
        if token.dep_ in ('nsubj', 'nsubjpass'):
            subj = token
            for child in token.head.children:
                if child.dep_ == 'dobj':
                    verb = token.head
                    obj = child
                    return subj.text, verb.lemma_, obj.text
    return subj.text if subj else '', verb.lemma_ if verb else '', obj.text if obj else ''

# Main function
def analyze_headline(headline):
    articles = fetch_google_headlines(headline)
    similarity_score, best_article = compute_similarity(headline, articles)

    h_subj, h_verb, h_obj = extract_svo(headline)
    m_subj, m_verb, m_obj = extract_svo(best_article['title']) if best_article else ('', '', '')

    prediction = "FAKE"

    if similarity_score >= 0.7:
        if (h_subj.lower() in m_subj.lower() or m_subj.lower() in h_subj.lower()) or (h_obj.lower() in m_obj.lower() or m_obj.lower() in h_obj.lower()):
            prediction = "REAL"
        elif h_subj and h_obj and not m_subj and not m_obj:
            prediction = "REAL"
    elif similarity_score >= 0.85:
        prediction = "REAL"

    return {
        "headline": headline,
        "similarity_score": similarity_score,
        "prediction": prediction,
        "matching_articles": articles
    }

# ✅ Optional test when run directly
if __name__ == "__main__":
    headline = input("Enter a news headline: ")
    result = analyze_headline(headline)
    print("Prediction:", result["prediction"])
    print("Similarity Score:", result["similarity_score"])
    print("Top Matches:")
    for article in result["matching_articles"]:
        print(f"- {article['title']}")
        print(f"  🔗 {article['url']}")
