from scanner.image_scanner import load_exif_data,analyze_image_metadata
from risk.risk_engine import evaluate_image_risk
from cleaner.image_cleaner import clean_image_metadata
path=input("Enter the path of the image: ")
metadata=load_exif_data(path)
analysis=analyze_image_metadata(metadata)
risk=evaluate_image_risk(analysis)
print(metadata)
print("\n-------Risk Report---------")
print("Risk Score:", risk["score"])
print("Risk Level:", risk["risk_level"])
print("\nReasons:")
print("ANALYSIS:", analysis)
for r in risk["reasons"]:
    print("-",r)
choice = input("clean this image? (y/n): ")
if choice == "y" or choice == "Y":
    new_path=clean_image_metadata(path)
    print("Cleaned Image Path at :", new_path)

