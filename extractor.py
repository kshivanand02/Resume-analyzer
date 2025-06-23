import fitz  # PyMuPDF
import sys
import os

# Define skill keywords
TARGET_SKILLS = [
    "Python", "SQL", "Machine Learning", "Deep Learning", "Data Analysis",
    "Pandas", "NumPy", "TensorFlow", "Keras", "Scikit-learn", "NLP", "Power BI"
]

def extract_text_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        print("Error: File not found.")
        return ""
    
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def count_skills(text):
    skill_counts = {}
    lower_text = text.lower()

    for skill in TARGET_SKILLS:
        count = lower_text.count(skill.lower())
        skill_counts[skill] = count
    return skill_counts

def suggest_improvements(skill_counts):
    missing = [skill for skill, count in skill_counts.items() if count == 0]
    if not missing:
        return "✅ Resume covers all key skills."
    return "❗Consider adding or emphasizing these skills:\n" + ", ".join(missing)

def main():
    if len(sys.argv) < 2:
        print("Usage: python resume_analyzer.py <path_to_resume.pdf>")
        return

    pdf_path = sys.argv[1]
    print(f"🔍 Analyzing resume: {pdf_path}")

    text = extract_text_from_pdf(pdf_path)
    if not text.strip():
        print("No text extracted from the PDF.")
        return

    skill_counts = count_skills(text)

    print("\n📊 Skill Frequency Report:")
    for skill, count in skill_counts.items():
        print(f"{skill}: {count}")

    print("\n💡 Suggestions:")
    print(suggest_improvements(skill_counts))

if __name__ == "__main__":
    main()
