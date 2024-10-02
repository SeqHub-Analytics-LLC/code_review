import fitz  # PyMuPDF
import re

def extract_text_and_sections_with_headers(pdf_path):
    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()

    headers = re.findall(r'\n([A-Z][A-Z\s]+)\n', text)
    sections = re.split(r'\n[A-Z][A-Z\s]+\n', text)

    if len(headers) < len(sections):
        sections = sections[:len(headers)]
    elif len(headers) > len(sections):
        headers = headers[:len(sections)]

    return text, headers, sections

def extract_text_from_pdf(file_path):
    with fitz.open(file_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text

def extract_sections_with_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()

    headers = re.findall(r'\n([A-Z][A-Z\s]+)\n', text)
    sections = re.split(r'\n[A-Z][A-Z\s]+\n', text)

    if len(headers) < len(sections):
        sections = sections[:len(headers)]
    elif len(headers) > len(sections):
        headers = headers[:len(sections)]

    return headers, sections
