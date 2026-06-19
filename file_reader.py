import os
from docx import Document
from PyPDF2 import PdfReader


def read_file(path):

    extension = os.path.splitext(path)[1].lower()

    try:

        if extension == ".txt":

            with open(path, "r", errors="ignore") as f:
                return f.read()

        elif extension == ".docx":

            doc = Document(path)

            text = []

            for para in doc.paragraphs:
                text.append(para.text)

            return "\n".join(text)

        elif extension == ".pdf":

            reader = PdfReader(path)

            text = ""

            for page in reader.pages:
                text += page.extract_text() or ""

            return text

        return ""

    except Exception as e:

        print("FILE READ ERROR:", e)

        return ""