mbti_scores = {

    ("INTJ", "ENFP"): 95,
    ("ENFP", "INTJ"): 95,

    ("INFP", "ENFJ"): 90,
    ("ENFJ", "INFP"): 90,

    ("ISTJ", "ESTP"): 75,
    ("ESTP", "ISTJ"): 75,

    ("ENTJ", "INTJ"): 85,
    ("INTJ", "ENTJ"): 85
}

def get_mbti_score(mbti1, mbti2):

    if mbti1 == mbti2:
        return 80

    return mbti_scores.get((mbti1, mbti2), 50)