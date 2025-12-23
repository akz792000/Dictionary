import requests

# ---- For local Ollama ----
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1"  # Or any local model you have

def read_txt(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def write_txt(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

# Read files
resume_text = read_txt("resume.txt")
job_description = read_txt("job_description.txt")

prompt = f"""
You are a professional resume writer.

Rewrite the resume to match the job description.
- Keep all information truthful
- Invent experience if needed
- Optimize keywords for ATS
- Use concise bullet points

JOB DESCRIPTION:
{job_description}

CURRENT RESUME:
{resume_text}

OUTPUT:
Return ONLY the rewritten resume text.
"""

# ---- Local AI call ----
response = requests.post(
    OLLAMA_URL,
    json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    },
    timeout=120
)

tailored_resume = response.json()["response"]

# Save output
write_txt("tailored_resume.txt", tailored_resume)

print("✅ Tailored resume saved as tailored_resume.txt")
