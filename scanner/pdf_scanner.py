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
        pdf_analysis["creation_date"] = parse_pdf_date(metadata["CreationDate"])

    if "ModDate" in metadata:
        pdf_analysis["modification_date"] = parse_pdf_date(metadata["ModDate"])

    return pdf_analysis

def parse_pdf_date(date_string):
    if not date_string:
        return None
    if date_string.startswith("D"):
        date_string = date_string[2:]
        core=date_string[:14]
        year=core[:4]
        month=core[4:6]
        day=core[6:8]
        hour=core[8:10]
        minute=core[10:12]
        second=core[12:14]
        timezone=date_string[14:]
        if timezone:
            timezone_clean=timezone.replace("'","")
            timezone_clean=timezone_clean[:3]+":"+timezone_clean[3:]
        else:
            timezone_clean=""
        formated=f"{year}-{month}-{day} {hour}:{minute}:{second}"
        return f"{formated} (UTC{timezone_clean})"
