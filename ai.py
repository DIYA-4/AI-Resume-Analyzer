import pdfplumber

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

with pdfplumber.open("RESUME.pdf") as pdf:
    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

found_skills = []

for skill in skills_db:
    if skill.lower() in text.lower():
        found_skills.append(skill)

print("Skills Found:")
for skill in found_skills:
    print("-", skill)
    score = 0

if "skills" in text.lower():
    score += 20

if "education" in text.lower():
    score += 20

if "project" in text.lower():
    score += 20

if "experience" in text.lower():
    score += 20

if "@" in text:
    score += 20

print("\nATS Score:", score, "/100")
if score >= 80:
    print("Excellent Resume")
elif score >= 60:
    print("Good Resume")
else:
    print("Needs Improvement")
    
jd = input("Paste Job Description: ")
jd_skills = []

for skill in skills_db:
    if skill.lower() in jd.lower():
        jd_skills.append(skill)

print("\nJD Skills:")
for skill in jd_skills:
    print("-", skill)
    missing_skills = []

for skill in jd_skills:
    if skill not in found_skills:
        missing_skills.append(skill)

print("\nMissing Skills:")

if len(missing_skills) == 0:
    print("None")
else:
    for skill in missing_skills:
        print("-", skill)
        if len(jd_skills) > 0:
            match_score = (len(jd_skills) - len(missing_skills)) / len(jd_skills) * 100
        else:
            match_score = 0

        print(f"\nMatch Score: {match_score:.2f}%")

if len(jd_skills) > 0:
    match_score = (
        (len(jd_skills) - len(missing_skills))
        / len(jd_skills)
    ) * 100
else:
    match_score = 0

print(f"\nMatch Score: {match_score:.2f}%")

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity        

model = SentenceTransformer('all-MiniLM-L6-v2')
resume_embedding = model.encode([text])
jd_embedding = model.encode([jd])

score = cosine_similarity(
    resume_embedding,
    jd_embedding
)[0][0]

print(f"\nAI Match Score: {score*100:.2f}%")

print("\nSuggestions:")

if "experience" not in text.lower():
    print("- Add Experience Section")

if "projects" not in text.lower():
    print("- Add More Projects")

if len(found_skills) < 5:
    print("- Add More Technical Skills")