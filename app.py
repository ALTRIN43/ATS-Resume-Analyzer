import streamlit as st

from parser.pdf_parser import extract_text_from_pdf

from analyzer.skill_extractor import extract_skills

from analyzer.scorer import calculate_score

from analyzer.section_detector import detect_sections


st.set_page_config(
    page_title="ATS Resume Analyzer",
    layout="wide"
)

st.title("📄 ATS Resume Analyzer")

uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

jd_text = st.text_area(
    "Paste Job Description Here"
)

if uploaded_files and jd_text:

    with open("data/skills_db.txt") as f:

        skills_db = [
            line.strip()
            for line in f.readlines()
        ]

    jd_skills = extract_skills(
        jd_text,
        skills_db
    )

    results = []

    for uploaded_file in uploaded_files:

        resume_text = extract_text_from_pdf(
            uploaded_file
        )

        resume_skills = extract_skills(
            resume_text,
            skills_db
        )

        sections = detect_sections(
            resume_text
        )

        skill_score = calculate_score(
            resume_skills,
            jd_skills
        )

        section_score = (
            sum(sections.values())
            / len(sections)
        ) * 100

        overall_score = (
            skill_score * 0.8
            + section_score * 0.2
        )

        score = round(
            overall_score,
            2
        )

        matched = (
            resume_skills
            .intersection(jd_skills)
        )

        missing = (
            jd_skills
            - resume_skills
        )

        with st.expander(
            f"{uploaded_file.name} - {score}%"
        ):

            st.metric(
                "ATS Score",
                f"{score}%"
            )

            st.metric(
                "Section Score",
                f"{section_score:.0f}%"
            )

            st.write("### ✅ Matched Skills")

            st.write(
                sorted(list(matched))
            )

            st.write("### ❌ Missing Skills")

            st.write(
                sorted(list(missing))
            )

            st.write("### 📑 Sections")

            for section, exists in sections.items():

                if exists:
                    st.success(
                        f"{section.title()} ✓"
                    )

                else:
                    st.error(
                        f"{section.title()} ✗"
                    )

        results.append({
            "Resume": uploaded_file.name,
            "ATS Score": score
        })

    results = sorted(
        results,
        key=lambda x: x["ATS Score"],
        reverse=True
    )

    st.subheader(
        "🏆 Resume Rankings"
    )

    st.dataframe(
        results,
        use_container_width=True
    )