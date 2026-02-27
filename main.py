from scanner.image_scanner import load_exif_data,analyze_image_metadata
from scanner.pdf_scanner import load_pdf_metadata
from scanner.pdf_scanner import analyze_pdf_metadata
from risk.risk_engine import evaluate_image_risk
from cleaner.image_cleaner import clean_image_metadata
from risk.risk_engine import evaluate_pdf_risk
from cleaner.pdf_cleaner import clean_pdf_metadata
path = input("Enter the path of the file: ")
path_lower = path.lower()

if path_lower.endswith(".jpg") or path_lower.endswith(".jpeg"):
    metadata = load_exif_data(path)
    analysis = analyze_image_metadata(metadata)
    risk = evaluate_image_risk(analysis)

    print(metadata)
    print("\n-------Risk Report---------")
    print("Risk Score:", risk["score"])
    print("Risk Level:", risk["risk_level"])
    print("\nReasons:")
    print("ANALYSIS:", analysis)

    for r in risk["reasons"]:
        print("-", r)

    choice = input("Clean this image? (y/n): ")
    if choice.lower() == "y":
        new_path = clean_image_metadata(path)
        print("Cleaned Image Path at:", new_path)

elif path_lower.endswith(".pdf"):
    metadata = load_pdf_metadata(path)
    analysis = analyze_pdf_metadata(metadata)
    risk = evaluate_pdf_risk(analysis)

    print("\n======= PDF Privacy Report =======")
    print("Risk Score:", risk["score"])
    print("Risk Level:", risk["risk_level"])
    print("\nFindings:")

    for r in risk["reasons"]:
        print("-", r)

    choice = input("\nClean this PDF? (y/n): ")
    if choice.lower() == "y":
        new_path = clean_pdf_metadata(path)
        print("Cleaned PDF saved at:", new_path)

else:
    print("Unsupported file type.")



