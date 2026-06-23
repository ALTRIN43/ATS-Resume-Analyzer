import re

SECTION_HEADERS = {
    "education": [
        "education",
        "academic background",
        "qualification"
    ],

    "skills": [
        "skills",
        "technical skills",
        "core competencies"
    ],

    "projects": [
        "projects",
        "academic projects",
        "personal projects"
    ],

    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "internship"
    ],

    "certifications": [
        "certifications",
        "certificates",
        "licenses"
    ]
}


def detect_sections(text):

    text = text.lower()

    detected = {}

    for section, keywords in SECTION_HEADERS.items():

        found = False

        for keyword in keywords:

            pattern = rf"\b{re.escape(keyword)}\b"

            if re.search(pattern, text):
                found = True
                break

        detected[section] = found

    return detected