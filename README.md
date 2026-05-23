# 🤖 IntelliMatch AI

## Smart Profile Recommendation System using NLP

IntelliMatch AI is an intelligent profile recommendation system that matches users based on:

- Professional goals
- Personal interests
- Personality types (MBTI)
- Bio similarity using NLP

The system uses:
- TF-IDF Vectorization
- Cosine Similarity
- MBTI Compatibility Logic

to generate smart compatibility recommendations between users.

---

# 🚀 Features

✅ User Profile Matching  
✅ NLP-based Text Similarity  
✅ MBTI Personality Compatibility  
✅ Compatibility Percentage Score  
✅ Top 5 Smart Recommendations  
✅ Modern Streamlit UI  
✅ CSV-based Dataset System  
✅ Real-time Recommendation Engine  

---

# 🧠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend Logic |
| Streamlit | Frontend UI |
| Pandas | Data Handling |
| Scikit-learn | NLP & Similarity |
| TF-IDF | Text Vectorization |
| Cosine Similarity | Profile Matching |

---

# 📂 Project Structure

```bash
IntelliMatch-AI/
│
├── app.py
├── requirements.txt
│
├── data/
│   ├── users.csv
│   └── feedback.csv
│
├── src/
│   ├── preprocessing.py
│   ├── similarity.py
│   ├── mbti_match.py
│   └── recommendation.py
│
├── assets/
│   └── styles.css
│
└── screenshots/
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/IntelliMatch-AI.git
```

---

## 2. Navigate into Project Folder

```bash
cd IntelliMatch-AI
```

---

## 3. Create Virtual Environment

```bash
python3 -m venv venv
```

---

## 4. Activate Virtual Environment

### Mac/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 5. Install Requirements

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Project

```bash
streamlit run app.py
```

OR

```bash
python3 -m streamlit run app.py
```

---

# 📊 How It Works

## Step 1 — User Profiles

Users enter:
- profession
- bio
- interests
- MBTI personality type

---

## Step 2 — NLP Processing

The system:
- cleans text
- removes unnecessary words
- converts text into vectors using TF-IDF

---

## Step 3 — Similarity Calculation

Cosine Similarity is used to compare profile similarity mathematically.

### Formula

```math
Similarity = cos(θ)
```

---

## Step 4 — MBTI Compatibility

The system checks personality compatibility using predefined MBTI rules.

Example:
- INTJ + ENFP = High Match
- INFP + ENFJ = High Match

---

## Step 5 — Final Recommendation Score

Final compatibility score is calculated using:

```math
FinalScore = (0.7 × TextSimilarity) + (0.3 × MBTI)
```

---

# 📁 Dataset

## users.csv

Contains:
- user_id
- name
- profession
- mbti
- professional_summary
- about_me
- interests

---

## feedback.csv

Stores:
- accepted recommendations
- rejected recommendations

---

# 🖥️ Sample Output

```text
Top Match: Sneha
Compatibility: 92%

✔ Similar AI Interests
✔ Compatible Personality
✔ Similar Career Goals
```

---

# 🎯 Future Improvements

- Login Authentication
- SQLite Database
- AI Chat Assistant
- Profile Images
- Match Analytics Dashboard
- Adaptive Machine Learning
- Real-time Recommendation Learning

---

# 📌 Project Objective

The goal of IntelliMatch AI is to build a smart recommendation platform that understands human profiles semantically and recommends compatible users intelligently.
<img width="1470" height="956" alt="Screenshot 2026-05-19 at 6 42 27 PM" src="https://github.com/user-attachments/assets/0a63a906-055b-4595-92ab-922d0fcd4339" />
<img width="1470" height="956" alt="Screenshot 2026-05-19 at 6 42 20 PM" src="https://github.com/user-attachments/assets/eeb9300b-805a-46a0-b8c6-fce0c13ce873" />
<img width="1470" height="956" alt="Screenshot 2026-05-19 at 6 42 43 PM" src="https://github.com/user-attachments/assets/968d5adb-0fa2-4a8c-9f30-ed4f8ee39413" />
<img width="1470" height="956" alt="Screenshot 2026-05-19 at 6 42 11 PM" src="https://github.com/user-attachments/assets/c6fca7fb-e452-408d-bf42-c01dae042260" />
<img width="1470" height="956" alt="Screenshot 2026-05-19 at 6 43 13 PM" src="https://github.com/user-attachments/assets/40af6c8d-3012-4d85-8772-478fd08b0a95" />

---

# 👨‍💻 Author

Developed by Chethan R

---

# ⭐ GitHub

If you like this project, give it a ⭐ on GitHub!
