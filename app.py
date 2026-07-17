import streamlit as st
import pdfplumber
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


skills_db = [
    "Python",
    "Java",
    "SQL",
    "MySQL",
    "JDBC",
    "Machine Learning",
    "Deep Learning",
    "React",
    "Docker",
    "AWS",
    "Git",
    "Linux"
]


# Extract Resume Text
def extract_text(pdf_file):

    text = ""

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text



# Find Skills
def find_skills(text):

    found = []

    for skill in skills_db:

        if skill.lower() in text.lower():
            found.append(skill)

    return found




jd_skills = []

for skill in skills_db:
    if skill.lower() in jd.lower():
        jd_skills.append(skill)

missing_skills = []

for skill in jd_skills:
    if skill not in skills:
        missing_skills.append(skill)



# ATS Score
def ats_score(text):

    score = 0

    sections = [
        "skills",
        "education",
        "project",
        "experience",
        "@"
    ]

    for section in sections:

        if section in text.lower():
            score += 20

    return score



# AI Similarity
def ai_match(resume,jd):

    model = SentenceTransformer(
        'all-MiniLM-L6-v2'
    )

    resume_embedding = model.encode([resume])

    jd_embedding = model.encode([jd])


    similarity = cosine_similarity(
        resume_embedding,
        jd_embedding
    )[0][0]


    return similarity*100



# UI


st.title("🤖 AI Resume Analyzer")

st.write(
    "Upload your resume and compare it with Job Description"
)


resume = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)


jd = st.text_area(
    "Paste Job Description"
)



if st.button("Analyze Resume"):


    if resume and jd:


        text = extract_text(resume)


        skills = find_skills(text)


        score = ats_score(text)


        ai_score = ai_match(
            text,
            jd
        )


        st.success(
            "Analysis Completed!"
        )


        col1,col2,col3 = st.columns(3)


        with col1:
            st.metric(
                "ATS Score",
                f"{score}/100"
            )


        with col2:
            st.metric(
                "Skills Found",
                len(skills)
            )


        with col3:
            st.metric(
                "AI Match",
                f"{ai_score:.2f}%"
            )



        st.subheader(
            "Technical Skills"
        )


        for skill in skills:
            st.write(
                "✅",
                skill
            )



        st.subheader(
            "Suggestions"
        )


        if "experience" not in text.lower():

            st.warning(
                "Add Experience Section"
            )


        if len(skills)<5:

            st.warning(
                "Add More Technical Skills"
            )


    else:

        st.error(
            "Please upload resume and add JD"
        )