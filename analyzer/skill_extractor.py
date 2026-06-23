# analyzer/skill_extractor.py

import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

def extract_skills(text, skills_db):

    matcher = PhraseMatcher(
        nlp.vocab,
        attr="LOWER"
    )

    patterns = [
        nlp.make_doc(skill)
        for skill in skills_db
    ]

    matcher.add("SKILLS", patterns)

    doc = nlp(text)

    matches = matcher(doc)

    found_skills = set()

    for match_id, start, end in matches:
        found_skills.add(
            doc[start:end].text.lower()
        )

    return found_skills