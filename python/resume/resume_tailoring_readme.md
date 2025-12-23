# Resume Tailoring App

This Python application takes your existing resume and a job description, then generates a **tailored resume** optimized for that specific job.  
It works locally with TXT files and **no paid API required** using Ollama.

# Features

### 1. Reads `resume.txt` and `job_description.txt` from the current folder
### 2. Generates `tailored_resume.txt` optimized for the job description
### 3. Preserves bullet points and plain text formatting
### 4. Fully local: no paid API required
### 5. Works inside a Python `.venv`

# Prerequisites

### 1. Python 3.11+
### 2. Ollama installed (local AI model)

# Installation Instructions

### 1. Install Homebrew (macOS only)

Homebrew is a package manager for macOS that makes it easy to install software.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Install Python 3 and pip

Python 3 comes with pip, a package manager for Python. Install Python 3 using Homebrew:

```bash
brew install python
```

### 3. Set Up a Virtual Environment

Using a virtual environment is a best practice for managing project-specific dependencies.

```bash
# Navigate to your project directory or create a new one:
mkdir resume-tailoring
cd resume-tailoring

# Create a virtual environment named .venv
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install required Python package
pip install requests
```

### 4. Install Ollama and Download a Model

```bash
brew install ollama
ollama pull llama3.1
```

If the Ollama server does not start automatically, start it manually:

```bash
ollama serve
```

### 5. Create Your Python Script

Create a file called `generate_resume.py` with the following content:

```python
import requests

# ---- Local Ollama API ----
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1"

def read_txt(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def write_txt(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

# Read inputs
resume_text = read_txt("resume.txt")
job_description = read_txt("job_description.txt")

prompt = f"""
You are a professional resume writer.

Rewrite the resume to match the job description.
- Keep all information truthful
- Do NOT invent experience
- Optimize keywords for ATS
- Use concise bullet points

JOB DESCRIPTION:
{job_description}

CURRENT RESUME:
{resume_text}

OUTPUT:
Return ONLY the rewritten resume text.
"""

# Call local AI
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
```

### 6. Run Your Script

```bash
# Make sure your virtual environment is active
source .venv/bin/activate

# Run the Python script
python generate_resume.py
```

The tailored resume will be saved as:

```
tailored_resume.txt
```

# Uninstallation Instructions

### 1. Deactivate the Virtual Environment

```bash
deactivate
```

### 2. Remove the Virtual Environment Directory

```bash
rm -rf .venv
```

### 3. Uninstall Python Packages (if needed)

```bash
source .venv/bin/activate
pip uninstall requests
deactivate
```

### 4. Uninstall Ollama

```bash
brew uninstall ollama
```

### 5. Uninstall Python 3 and Homebrew (optional)

```bash
brew uninstall python

# Optional: uninstall Homebrew (if not used for other packages)
#/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"
```

# Example Folder Structure

```
resume-tailoring/
├── .venv/
├── generate_resume.py
├── resume.txt
├── job_description.txt
├── tailored_resume.txt
```

# Example resume.txt

```
Name: John Doe
Experience:
- Software Engineer at XYZ Corp (2018-2023)
- Developed REST APIs and backend services
Skills:
- Python, SQL, Docker
Education:
- B.Sc. Computer Science
```

# Example job_description.txt

```
Looking for a Backend Engineer with experience in Python, API development, and Docker. Must have strong problem-solving skills and knowledge of cloud infrastructure.
```

