from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

def train_model(df):
    tfidf = TfidfVectorizer(stop_words='english')

    X = tfidf.fit_transform(df['message'])
    y = df['label']

    model = MultinomialNB()
    model.fit(X, y)

    return model, tfidf

def predict(text, model, tfidf):
    vector = tfidf.transform([text])
    result = model.predict(vector)[0]

    if result == 1:
        return "Spam detected 🚫"
    else:
        return "Not Spam detected ✅"