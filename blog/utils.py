import random
import re
import unicodedata
import string
from pathlib import Path
from flask import current_app
from blog import app
from PIL import Image

ALPHA_NUMERIC_CHARS = string.ascii_letters+string.digits
STRING_LENGTH = 6
UPLOAD_FOLDER = app.config["UPLOAD_FOLDER"]

def generate_random_string(chars=ALPHA_NUMERIC_CHARS, length=STRING_LENGTH):
    return "".join(random.choice(chars) for _ in range(length))

def slugify(value):
    value = str(value)
    value = unicodedata.normalize("NFKD", value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[\s-]', '-', value)

def title_slugifier(post_title):
    return f"{slugify(post_title)}-{generate_random_string()}"

def save_picture(form_data):
    filename = form_data.filename
    picture_name = f"{generate_random_string()}-{filename}"
    pic_path = Path(current_app.root_path) / UPLOAD_FOLDER / picture_name
    
    image = Image.open(form_data)
    image.save(pic_path)
    return picture_name