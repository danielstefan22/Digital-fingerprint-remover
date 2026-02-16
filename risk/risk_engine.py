from scanner.image_scanner import analyze_image_metadata
#function for scoring and evaluating risk levels in images
def evaluate_image_risk(analysis):
    score=0
    reasons=[]
    risk_level=""
    if analysis["has_gps"]:
        score+=50
        reasons.append("GPS information exposed")
    if analysis["camera_model"]is not None:
        score+=15
        reasons.append("Camera model exposed")
    if analysis["timestamp"]is not None:
        score+=10
        reasons.append("Timestamp exposed")
    if score == 0:
        reasons.append("No risk found")
        risk_level="SAFE"
    elif 0<score<=20:
        risk_level="LOW"
    elif 20<score<=50:
        risk_level="MEDIUM"
    elif 50<score<=100:
        risk_level="HIGH"
    return {"score" : score,"reasons" : reasons,"risk_level" : risk_level}
