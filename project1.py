import streamlit as st

st.title("AI Resume Analyzer")

resume = st.text_area("Paste Resume")
jd = st.text_area("Paste Job Description")

if st.button("Analyze"):
    resume_words = set(resume.lower().split())
    jd_words = set(jd.lower().split())

    matched = resume_words.intersection(jd_words)

    score = int((len(matched)/max(len(jd_words),1))*100)

    st.write(f"ATS Score: {score}%")

    missing = jd_words - resume_words

    st.write("Missing Keywords:")
    st.write(list(missing)[:20])