from PIL import Image
import os
def clean_image_metadata(image_path):
    image = Image.open(image_path)
    data=image.getdata()
    clean_image=Image.new(image.mode, image.size)
    clean_image.putdata(data)
    name,ext=os.path.splitext(image_path)
    new_path=name+"_cleaned"+ext
    clean_image.save(new_path)
    return new_path