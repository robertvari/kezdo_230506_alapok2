from my_functions.get_all_files import get_all_files
from PIL import Image, ImageDraw, ImageFont
import os

def main(root_folder, text, font_size=40):
    files = []
    get_all_files(root_folder, files, file_ext=".jpg")
    
    new_image = process_image(files[0], text, font_size)
    save_image(new_image, files[0])

def save_image(new_image, filename):
    root_folder = os.path.dirname(filename)
    base_name = os.path.basename(filename)
    
    save_dir = os.path.join(root_folder, "_thumbnail")
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    new_file_name = os.path.join(save_dir, base_name)
    new_image.save(new_file_name)

    

def process_image(image_file, text, font_size):
    photo = image_file
    # open image and convert it to RGBA
    img = Image.open(photo).convert("RGBA")

    # resize image
    img.thumbnail((1000, 1000))
    img_width = img.size[0]
    img_height = img.size[1]
    
    # create an empty canvas layer
    text_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(text_layer)

    font = ImageFont.truetype("watermarker.ttf", font_size)
    text_box = font.getbbox(text)
    text_width = text_box[2]
    text_height = text_box[3]

    margin = 20

    x = img_width - text_width - margin
    y = img_height -text_height- margin
    draw.text((x, y), text, fill=(255, 255, 255, 100), font=font)
    
    img = Image.alpha_composite(img, text_layer).convert("RGB")
    return img



main(r"D:\Work\_PythonSuli\kezdo_230506\photos", "Rödönyi Photo")