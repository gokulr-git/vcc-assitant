from flask import Flask, render_template, request, send_file
import google.generativeai as genai  # ✅ Correct
from google.generativeai import types 
import base64
import os
import tempfile

app = Flask(__name__)

# Configure Vertex AI
genai.configure(
    vertexai=True,
    project="",
    location="us-central1",
)

# System Prompt
system_prompt = "Act as an expert HR assistant. You will be given the text content of a resume..."

# Analysis Prompt (simplified for this example)
analysis_prompt = """
Analyze the following resume text against the four criteria...
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        uploaded_file = request.files['resume']
        if uploaded_file.filename.endswith('.pdf'):
            pdf_bytes = uploaded_file.read()
            base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')

            contents = [
                types.Content(
                    role="user",
                    parts=[
                        types.Part.from_text(analysis_prompt),
                        types.Part.from_bytes(data=base64.b64decode(base64_pdf), mime_type="application/pdf")
                    ]
                )
            ]

            config = types.GenerateContentConfig(
                temperature=1,
                top_p=0.95,
                max_output_tokens=8192,
                system_instruction=[types.Part.from_text(system_prompt)],
                response_modalities=["TEXT"]
            )

            client = genai.Client()
            output = ""
            for chunk in client.models.generate_content_stream(
                model="gemini-2.0-flash-001",
                contents=contents,
                config=config
            ):
                output += chunk.text

            # Save to temp .txt file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode='w') as f:
                f.write(output)
                report_path = f.name

            return send_file(report_path, as_attachment=True, download_name="resume_report.txt")

    return render_template('index.html', result=result)
