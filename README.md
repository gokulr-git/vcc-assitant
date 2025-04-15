# vcc-assitant
 Smart Resume Analyzer using Vertex AI & GCP project. It’s structured to help others understand, use, and even contribute to the project:

⸻



# 🔍 Smart Resume Analyzer & Job Matcher using Vertex AI & GCP

A serverless, cloud-native resume parsing and job matching solution built using **Google Cloud Platform (GCP)**, **Document AI**, and **Vertex AI**. This project analyzes resumes uploaded via a web interface, provides instant insights and job match recommendations, and returns a downloadable evaluation report — all without storing any data.



## 📌 Features

- 🧾 **Resume Parsing** with Google Document AI
- 💡 **Intelligent Analysis** using Gemini 2.0 Flash (Vertex AI)
- 📄 **Real-time Recommendations & Scoring**
- ☁️ Fully **serverless and scalable** via Cloud Run
- 🔒 **No storage** of user resumes or data
- 📥 Downloadable result report in plain text or PDF

---

## 🛠️ Tech Stack

| Layer            | Tools/Services Used                                |
|------------------|----------------------------------------------------|
| Frontend         | HTML, CSS, Bootstrap                               |
| Backend          | Flask (Python)                                     |
| Cloud Platform   | Google Cloud Platform                              |
| Resume Parsing   | Google Document AI                                 |
| Intelligence     | Vertex AI Gemini (Prompt Engineering)              |
| Deployment       | Cloud Run, Cloud Shell                             |

---

## 📂 Project Structure

```bash
├── app.py                      # Flask backend
├── templates/
│   └── index.html              # Upload and result UI
├── static/
│   └── styles.css              # Custom styles
├── prompt_template.txt        # Prompt for Vertex AI
├── requirements.txt           # Python dependencies
├── Dockerfile                 # For Cloud Run deployment
└── README.md



⸻

✅ How It Works
	1.	User uploads a resume in PDF format.
	2.	Flask backend sends resume to Document AI for parsing.
	3.	Parsed content is sent to Vertex AI Gemini with a custom prompt.
	4.	Gemini generates:
	•	Resume Summary
	•	Skill Classification
	•	Job Role Fitment
	•	Improvement Recommendations
	5.	Output is displayed instantly on the web UI.
	6.	Option to download a plain-text report.

⸻

📦 Deployment Guide

Step 1: Enable GCP APIs

Enable the following APIs:
	•	Document AI API
	•	Vertex AI API
	•	Cloud Run
	•	Cloud Build

gcloud services enable documentai.googleapis.com
gcloud services enable aiplatform.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com

Step 2: Clone and Set Up

git clone https://github.com/yourusername/smart-resume-analyzer.git
cd smart-resume-analyzer

Step 3: Build and Deploy to Cloud Run

gcloud builds submit --tag gcr.io/PROJECT-ID/resume-analyzer
gcloud run deploy resume-analyzer \
  --image gcr.io/PROJECT-ID/resume-analyzer \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated

Replace PROJECT-ID with your GCP project ID.

⸻

🧪 Sample Prompt Used (Vertex AI Gemini)

Analyze the following resume text against the four criteria listed below, ensuring your assessment language is professional and avoids informal abbreviations or slang. Strictly adhere to the specified output structure, placing each element on a separate line. Use the example output provided below as a guide for formatting.

Assessment Criteria:

Degree: Does the resume explicitly state a completed Bachelor's degree (B.E, B.Tech, Bsc, BCA)in 'Computer Science'

Experience: Does the work history (job titles, companies, dates) show a total professional work experience of at least 2 years? Calculate the duration based only on the start/end dates provided for roles listed after any mentioned university graduation date (if available).

Python Knowledge: Is the skill 'Python' explicitly mentioned anywhere in the resume (e.g., in a 'Skills' section or within job descriptions)?

Basic Information: Does the resume contain plausible text for a candidate name, an email address (containing '@' and '.'), and a phone number (sequence of digits, possibly with hyphens or parentheses)?




⸻

📈 Results
	•	⏱️ Avg. Evaluation Time: ~4 seconds
	•	📂 File Size Handled: Up to 7MB PDF
	•	🧠 Intelligence Source: Gemini 2.0 Flash
	•	🔒 Zero data stored: Fully ephemeral processing

⸻

🧾 References
	•	Resume Analyzer – IJSREM, April 2024
	•	Google Document AI Docs
	•	Vertex AI Gemini Prompting Docs
	•	Flask Official Documentation

⸻

🎯 Future Enhancements
	•	Add role-specific evaluation profiles
	•	Integrate job board APIs (LinkedIn, Indeed)
	•	Generate PDF feedback reports
	•	Enable login/usage analytics (with user consent)


📬 Contact

Built by Gokul,Puja,Richard | M.Tech in Data & Computational Science, IIT Jodhpur



