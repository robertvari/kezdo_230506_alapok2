from my_functions.get_all_files import get_all_files
from PIL import Image, ImageDraw, ImageFont

def main(root_folder, text, font_size=40):
    files = []
    get_all_files(root_folder, files, file_ext=".jpg")
    process_images(files, text, font_size)

def process_images(files, text, font_size):
    photo = files[0]
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
    img.show()



main(r"D:\Work\_PythonSuli\kezdo_230506\photos", "Rödönyi Photo")