from scanner.image_scanner import load_exif_data,analyze_image_metadata
from risk.risk_engine import evaluate_image_risk
path=input("Enter the path of the image: ")
metadata=load_exif_data(path)
analysis=analyze_image_metadata(metadata)
risk=evaluate_image_risk(analysis)
print("\n-------Risk Report---------")
print("Risk Score:", risk["score"])
print("Risk Level:", risk["risk_level"])
print("\nReasons:")
for r in risk["reasons"]:
    print("-",r)

