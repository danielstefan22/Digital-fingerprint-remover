from PIL import Image
from PIL.ExifTags import TAGS,GPSTAGS
def load_exif_data(image_path):
    opened_image = Image.open(image_path)
    exif_data = opened_image.getexif()
    metadata = {}
    if not exif_data:
        return {}
    for tag, value in exif_data.items():
        decoded = TAGS.get(tag, tag)
        metadata[decoded] = value
    return metadata
def analyze_image_metadata(metadata):
    analysis = {
        "has_gps": False,
        "camera_model": None,
        "timestamp": None
    }
    if "GPSInfo" in metadata:
        analysis["has_gps"]=True
    if "Model" in metadata:
        analysis["camera_model"] = metadata["Model"]
    if "DateTime" in metadata:
        analysis["timestamp"] = metadata["DateTime"]
    return analysis