# OCR Setup and Usage on macOS

This guide provides step-by-step instructions for setting up and uninstalling the necessary tools
and packages for Optical Character Recognition (OCR) on a macOS system.

## Installation Instructions

### 1. Install Homebrew

Homebrew is a package manager for macOS that makes it easy to install software. Install Homebrew
using the following command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
### 2. Install Python 3 and pip

Python 3 comes with pip, which is a package manager for Python. Install Python 3 using Homebrew:

```bash
brew install python
```
### 3. Install Tesseract OCR

Tesseract is an OCR engine that is used to read text from images. Install Tesseract using Homebrew:

```bash
brew install tesseract

# support language
brew install tesseract-lang
```
### 4. Set Up a Virtual Environment

Using a virtual environment is a good practice for managing project-specific dependencies.

```bash
# Navigate to your project directory or create a new one:
mkdir my_project
cd my_project

# Create a virtual environment
python3 -m venv myenv

# Activate the virtual environment
source myenv/bin/activate

# Install pytesseract and Pillow
pip install pytesseract Pillow
```
### 5. Create and Run Your Python Script

```bash
python3 read-image.py
``` 
Uninstallation Instructions

### 1. Deactivate the Virtual Environment

If you are currently in the virtual environment, deactivate it.

```bash
deactivate
```
### 2. Remove the Virtual Environment Directory

Delete the virtual environment directory if you no longer need it.

```bash
rm -rf myenv
```
### 3. Uninstall Python Packages

You can uninstall the Python packages from the virtual environment if needed.
Activate the virtual environment:

```bash
source myenv/bin/activate
Uninstall pytesseract and Pillow:
```

```bash
pip uninstall pytesseract Pillow
```
Deactivate the virtual environment:

```bash
deactivate
```

### 4. Uninstall Tesseract OCR

If you no longer need Tesseract OCR, you can uninstall it.

```bash
brew uninstall tesseract
```

### 5. Uninstall Python 3 and Homebrew (optional)

If you no longer need Python 3 and Homebrew, you can uninstall them as well.

Uninstall Python 3 using Homebrew:

```bash
brew uninstall python
```
Uninstall Homebrew (optional; not recommended if you use it for other packages):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"
```