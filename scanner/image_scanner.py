from PIL import Image
from PIL.ExifTags import TAGS,GPSTAGS
#helper function to calculate the longitute latitude
def dms_to_decimal(dms_tuple):
    degrees, minutes, seconds = dms_tuple
    return float(degrees + (minutes / 60) + (seconds / 3600))
#load exif data from images function
def load_exif_data(image_path):
    opened_image = Image.open(image_path)
    exif_data = opened_image._getexif()
    metadata = {}
    if not exif_data:
        return {}
    for tag, value in exif_data.items():
        decoded = TAGS.get(tag, tag)
        if decoded=="GPSInfo":
            gps_data = {}
            for gps_tag, gps_value in value.items():
                sub_decoded = GPSTAGS.get(gps_tag, gps_tag)
                gps_data[sub_decoded] = value[gps_tag]
            metadata["GPSInfo"] = gps_data
        else:
            metadata[decoded] = value
    return metadata
#analysis function to be used later in risk assessment
def analyze_image_metadata(metadata):

    analysis = {
        "has_gps": False,
        "camera_model": None,
        "timestamp": None,
        "software_info": None,
        "gps_latitude": None,
        "gps_longitude":None
    }
    if "GPSInfo" in metadata:
        analysis["has_gps"]=True
        gps_info = metadata["GPSInfo"]
        lat = gps_info.get("GPSLatitude")
        lat_ref = gps_info.get("GPSLatitudeRef")
        lon = gps_info.get("GPSLongitude")
        lon_ref = gps_info.get("GPSLongitudeRef")
        if lat and lat_ref:
            decimal_lat = dms_to_decimal(lat)
            if lat_ref == "S":
                decimal_lat = -decimal_lat
            analysis["gps_latitude"] = decimal_lat
        if lon and lon_ref:
            decimal_lon = dms_to_decimal(lon)
            if lon_ref == "W":
                decimal_lon = -decimal_lon
            analysis["gps_longitude"] = decimal_lon

    if "Model" in metadata:
        analysis["camera_model"] = metadata["Model"]
    if "DateTime" in metadata:
        analysis["timestamp"] = metadata["DateTime"]
    if "Software" in metadata:
        analysis["software_info"] = metadata["Software"]
    return analysis



