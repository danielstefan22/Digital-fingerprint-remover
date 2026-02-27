from PyPDF2 import PdfReader, PdfWriter, PdfFileReader, PdfFileWriter
import os
def clean_pdf_metadata(file_path):
    reader = PdfReader(file_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.add_metadata({})

    base, ext = os.path.splitext(file_path)
    new_path = f"{base}_cleaned{ext}"

    with open(new_path, "wb") as f:
        writer.write(f)

    return new_path