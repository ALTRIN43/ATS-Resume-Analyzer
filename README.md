<img width="1845" height="598" alt="image" src="https://github.com/user-attachments/assets/903813a9-22da-4ba8-a833-3901ac84de3e" /># ATS Resume Analyzer

## Overview

ATS Resume Analyzer is a web-based application that evaluates resumes against a given job description and provides an ATS compatibility score. The system extracts information from PDF resumes, identifies relevant skills, detects key resume sections, highlights missing requirements, and ranks multiple candidates based on their alignment with job requirements.

The project is designed to simulate a recruiter-style screening workflow and help candidates optimize their resumes for Applicant Tracking Systems (ATS).

## Features

* Upload and analyze multiple PDF resumes simultaneously
* Compare resumes against a custom job description
* Extract technical skills from resumes and job descriptions
* Calculate ATS compatibility scores using a weighted scoring mechanism
* Identify matched and missing skills
* Detect important resume sections such as:

  * Education
  * Skills
  * Projects
  * Experience
  * Certifications
* Rank candidates based on ATS scores
* Provide detailed analysis for each uploaded resume
* Modular architecture for future AI and NLP enhancements

## Project Architecture

```text
Resume PDFs
     |
     v
PDF Parser
     |
     v
Text Extraction
     |
     +------------------+
     |                  |
     v                  v
Skill Extractor   Section Detector
     |                  |
     +--------+---------+
              |
              v
         ATS Scoring
              |
              v
      Candidate Ranking
              |
              v
        Analysis Report
```

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Libraries

* pdfplumber
* Streamlit
* Regular Expressions (Regex)

### Planned Integrations

* spaCy
* Google Gemini API
* Matplotlib
* ReportLab

## Folder Structure

```text
ATS_Resume_Analyzer/
│
├── app.py
│
├── analyzer/
│   ├── skills.py
│   ├── scorer.py
│   └── section_detector.py
│
├── parser/
│   └── pdf_parser.py
│
└── data/
    └── skills_db.txt
```



## Installation

Clone the repository:

```bash
git clone <repository-url>
cd ATS_Resume_Analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit pdfplumber
```

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## How It Works

### Step 1: Upload Resumes

Upload one or more PDF resumes.

### Step 2: Enter Job Description

Paste the target job description into the input field.

### Step 3: Resume Analysis

The system:

* Extracts text from resumes
* Extracts relevant skills
* Detects resume sections
* Compares skills against the job description
* Computes ATS scores
* Ranks candidates

### Step 4: Results

The application displays:

* ATS Score
* Matched Skills
* Missing Skills
* Section Analysis
* Candidate Ranking

## ATS Scoring Methodology

The overall score is calculated using:

```text
Overall ATS Score =
(0.8 × Skill Match Score)
+
(0.2 × Section Completeness Score)
```

### Skill Match Score

Measures how many required job description skills are present in the resume.

### Section Completeness Score

Evaluates the presence of critical resume sections:

* Education
* Skills
* Projects
* Experience
* Certifications

## Example Output

```text
ATS Score: 84%

Matched Skills:
- Python
- SQL
- AWS
- Git

Missing Skills:
- Docker
- Kubernetes

Detected Sections:
- Education
- Skills
- Projects
- Certifications

Missing Sections:
- Experience
```

<img width="1740" height="816" alt="Screenshot 2026-06-23 144636" src="https://github.com/user-attachments/assets/ea92ee74-4fb8-425d-accb-991917499f90" />


## Future Enhancements

### NLP-Based Skill Extraction

Replace keyword matching with spaCy PhraseMatcher and Named Entity Recognition.

### AI-Powered Resume Recommendations

Integrate Google Gemini API to generate:

* Resume improvement suggestions
* Missing skill recommendations
* Project recommendations
* ATS optimization guidance

### PDF Report Generation

Generate downloadable ATS reports containing:

* Candidate details
* ATS score
* Skill analysis
* Improvement suggestions

### Advanced Analytics Dashboard

* Candidate leaderboards
* Skill distribution analysis
* ATS score visualizations
* Recruiter insights dashboard

### Semantic Job Matching

Implement embedding-based similarity matching to improve resume-job alignment accuracy.

## Potential Use Cases

* Candidate Resume Screening
* Recruitment Automation
* Resume Optimization
* Career Guidance Platforms
* HR Analytics Solutions
* Job Application Assistance



## Author

Altrin Jesuraj

B.Tech Artificial Intelligence
SRM Institute of Science and Technology

## License

This project is intended for educational, research, and portfolio purposes.
