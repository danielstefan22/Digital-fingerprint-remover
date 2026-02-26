from PyPDF2 import PdfReader, PdfFileReader

#load metadata
def load_pdf_metadata(file_path):
    reader = PdfReader(file_path)
    metadata = reader.metadata
    if not metadata:
        return{}
    normalized={}
    for key,value in metadata.items():
        clean_key=key.lstrip("/")
        normalized[clean_key]=value
    return normalized
#analize given metadata
def analyze_pdf_metadata(metadata):
    pdf_analysis = {
        "creator": None,
        "producer": None,
        "creation_date": None,
        "modification_date": None
    }

    if "Creator" in metadata:
        pdf_analysis["creator"] = metadata["Creator"]

    if "Producer" in metadata:
        pdf_analysis["producer"] = metadata["Producer"]

    if "CreationDate" in metadata:
        pdf_analysis["creation_date"] = metadata["CreationDate"]

    if "ModDate" in metadata:
        pdf_analysis["modification_date"] = metadata["ModDate"]

    return pdf_analysis