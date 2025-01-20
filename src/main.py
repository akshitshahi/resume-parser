# main.py

import docx
import os

# Function to extract text from docx files
def extract_text_from_docx(file_path):
    try:
        doc = docx.Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    except Exception as e:
        return f"Error: {e}"

# Function to parse a resume and extract key details
def parse_resume(file_path):
    text = extract_text_from_docx(file_path)
    if "Education" in text:
        print("Education section found.")
    if "Skills" in text:
        print("Skills section found.")
    if "Experience" in text:
        print("Experience section found.")
    return text

# Example usage
if __name__ == "__main__":
    file_path = 'path_to_resume.docx'  # Provide your docx file path here
    resume_text = parse_resume(file_path)
    print(resume_text)
