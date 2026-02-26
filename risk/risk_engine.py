from scanner.image_scanner import analyze_image_metadata
from scanner.pdf_scanner import analyze_pdf_metadata
#function for scoring and evaluating risk levels in images
def evaluate_image_risk(analysis):
    score=0
    reasons=[]
    risk_level=""
    if analysis["gps_latitude"] is not None and analysis["gps_longitude"] is not None:
        score+=50
        lat=analysis["gps_latitude"]
        lon=analysis["gps_longitude"]
        reasons.append(f"Exact location exposed:{lat:.6f} , {lon:.6f} ")
        reasons.append(f"Google Maps link: https://www.google.com/maps?q={lat:.6f},{lon:.6f}")
    if analysis["camera_model"]is not None:
        score+=15
        reasons.append("Camera model exposed")
    if analysis["timestamp"]is not None:
        score+=10
        reasons.append("Timestamp exposed")
    if analysis["software_info"] is not None:
        score+=20
        reasons.append("Software info exposed")
    if score == 0:
        reasons.append("No risk found")
        risk_level="SAFE"
    elif 0<score<=20:
        risk_level="LOW"
    elif 20<score<=50:
        risk_level="MEDIUM"
    elif score>50:
        risk_level="HIGH"
    return {"score" : score,"reasons" : reasons,"risk_level" : risk_level}
def evaluate_pdf_risk(pdf_analysis):
    score=0
    reasons=[]
    risk_level=""
    if pdf_analysis["creator"] is not None:
        score+=15
        reasons.append(f"Document created with: {pdf_analysis['creator']}")
    if pdf_analysis["producer"] is not None:
        score+=10
        reasons.append(f"PDF generated using: {pdf_analysis['producer']}")
    if pdf_analysis["creation_date"] is not None:
        score+=10
        reasons.append(f"Document creation timestamp exposed: {pdf_analysis['creation_date']}")
    if pdf_analysis["modification_date"] is not None:
        score+=10
        reasons.append(f"Document modification timestamp exposed: {pdf_analysis['modification_date']}")
    if score == 0:
        risk_level="SAFE"
    elif 0<score<=20:
        risk_level="LOW"
    elif 20<score<=50:
        risk_level="MEDIUM"
    elif score>50:
        risk_level="HIGH"
    return {"score" : score,"reasons" : reasons,"risk_level" : risk_level}