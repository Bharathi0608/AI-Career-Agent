# pyrefly: ignore [missing-import]
from PyPDF2 import PdfReader

def read_resume(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text 