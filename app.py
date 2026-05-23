import streamlit as st
from src.recommendation import get_recommendations

st.set_page_config(
    page_title="IntelliMatch AI",
    layout="wide"
)

st.title("🤖 IntelliMatch AI")
st.subheader("Smart Profile Recommendation System")

user_id = st.selectbox(
    "Select User ID",
    ["U001", "U002", "U003", "U004", "U005"]
)

if st.button("Find Best Matches"):

    recommendations = get_recommendations(user_id)

    st.success("Top Matches Found!")

    for match in recommendations:

        st.markdown(
            f"""
            <div class="match-card">

            <h3>{match['name']}</h3>

            <p><b>Profession:</b> {match['profession']}</p>

            <p><b>MBTI:</b> {match['mbti']}</p>

            <p><b>Interests:</b> {match['interests']}</p>

            <h2>Compatibility: {match['score']}%</h2>

            </div>
            """,
            unsafe_allow_html=True
        )