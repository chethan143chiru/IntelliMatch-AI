import pandas as pd

from src.preprocessing import clean_text
from src.similarity import calculate_similarity
from src.mbti_match import get_mbti_score


def get_recommendations(current_user_id):

    df = pd.read_csv("data/users.csv")

    # Combine text fields
    df["combined_text"] = (
        df["professional_summary"] + " " +
        df["about_me"] + " " +
        df["interests"]
    )

    # Clean text
    df["combined_text"] = df["combined_text"].apply(clean_text)

    # Similarity matrix
    similarity_matrix = calculate_similarity(df["combined_text"])

    # Current user index
    current_index = df[df["user_id"] == current_user_id].index[0]

    scores = []

    for i in range(len(df)):

        if i == current_index:
            continue

        # NLP similarity score
        text_score = similarity_matrix[current_index][i] * 100

        # MBTI score
        mbti_score = get_mbti_score(
            df.iloc[current_index]["mbti"],
            df.iloc[i]["mbti"]
        )

        # Final combined score
        final_score = (
            (0.7 * text_score) +
            (0.3 * mbti_score)
        )

        scores.append({
            "name": df.iloc[i]["name"],
            "profession": df.iloc[i]["profession"],
            "mbti": df.iloc[i]["mbti"],
            "score": round(final_score, 2),
            "interests": df.iloc[i]["interests"]
        })

    # Sort by score descending
    scores = sorted(
        scores,
        key=lambda x: x["score"],
        reverse=True
    )

    return scores[:5]