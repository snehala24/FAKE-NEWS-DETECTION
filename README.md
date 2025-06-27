# 📰 FAKE NEWS DETECTION

This project aims to detect whether a given news article is **real** or **fake** using **real-time data** from Google News and NewsAPI. By leveraging machine learning techniques on freshly fetched articles, the system attempts to reduce the spread of misinformation and verify the credibility of news content.

---

## 🔍 Project Objective

The goal is to build an intelligent system that can:
- Fetch real-world news using APIs
- Analyze article content for fake news detection
- Provide results with a user-friendly interface or console

This avoids outdated datasets and enables up-to-date news verification.

---

## 🧠 Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Core programming |
| **NewsAPI / Google News API** | Fetch real-time news articles |
| **Requests** | API interaction |
| **NLTK / TextBlob** | Natural language processing |
| **Scikit-learn** | Model training & evaluation |
| **TfidfVectorizer** | Feature extraction |
| **Logistic Regression** | Binary classification model |
| **Flask / Streamlit** *(Optional)* | Frontend interface |
| **Jupyter Notebook** | Development and testing |

---

## 🔑 API Integration

The project uses:
- ✅ **NewsAPI**: To fetch articles from popular news sources  
  Docs: [https://newsapi.org/docs](https://newsapi.org/docs)
- ✅ **Google News API**: For extended search and real-time updates

You’ll need API keys to access these. Store them securely in a `.env` file or as environment variables.

---


---

## 🧹 Data Flow & Preprocessing

1. Use NewsAPI / Google API to fetch articles
2. Extract article `title`, `description`, or `content`
3. Preprocess:
   - Lowercase
   - Remove punctuation and stopwords
   - Tokenization, Lemmatization
4. Convert to TF-IDF features

---

## 🤖 Model Building

- **Algorithm**: Logistic Regression (or similar)
- **Pipeline**:
  - TF-IDF Vectorizer
  - Train-test split
  - Model training
  - Save as `model.pkl`

---

## 🧪 Model Evaluation

- Evaluated on real-time labeled data (manual or simulated)
- Metrics:
  - **Accuracy**
  - **Precision & Recall**
  - **Confusion Matrix**

Note: Since there's no static dataset, real-world evaluation depends on manually known fake/real examples.

---

## 🌐 Web App Interface (Optional)

If integrated with **Flask** or **Streamlit**, users can:
- Enter or select a news article
- Click **"Detect"**
- Get output: ✅ Real or ❌ Fake

---

## 📦 Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/snehala24/FAKE-NEWS-DETECTION
cd FAKE-NEWS-DETECTION

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your API keys to a .env file or environment variables
# Example .env:
# NEWS_API_KEY=your_api_key
# GOOGLE_API_KEY=your_google_key

