import re

# Simple stopwords list
stop_words = {
    "the", "is", "and", "in", "to",
    "of", "a", "for", "on", "with",
    "this", "that", "i", "am"
}


def clean_text(text):
    # Convert to string
    text = str(text)

    # Lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r"[^a-zA-Z ]", "", text)

    # Split words
    words = text.split()

    # Remove stopwords
    filtered_words = [
        word for word in words
        if word not in stop_words
    ]

    # Join words
    return " ".join(filtered_words)
