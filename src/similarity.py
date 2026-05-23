from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(user_texts):

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(user_texts)

    similarity_matrix = cosine_similarity(tfidf_matrix)

    return similarity_matrix