from PIL import Image
from dataclass import Genshin_Element
from io import BytesIO
import requests

#画像の背景色を作る
def backgroundcolor(color:tuple,width=1930,height=630):
    # 画像のサイズと色を指定する
    #炎：(204, 71, 51)
    #草：(59, 177, 0)
    #風：(45, 178, 162)
    #氷：(85, 185, 242)
    #水：(28, 128, 186)
    #雷：(170, 80, 229)
    #岩：(178, 139, 26)
    width = width
    height = height
    color = color

    # 画像を作成する
    img = Image.new("RGB", (width, height), color)

    # 画像を返す
    return img.convert('RGBA')

def convert_jpg_to_semi_transparent_png(grayscale_img_path:str="item\overlay.jpg"):
    # 画像を読み込む
    img = Image.open(grayscale_img_path).convert('RGBA')
    # 画像の不透明度を 70% に変更する
    alpha = 0.6
    img.putalpha(int(255 * alpha))

    # png 形式で保存する
    return img.convert('RGBA')

#背景画像とグレースケールを張り合わせる
def backgroundcreate(bacgroungcolor_img:Image.Image,grayscale_img:Image.Image):
    #リサイズする
    new_size = (1930, 630)
    gray_size = (1930, 630)

    back = bacgroungcolor_img.resize(new_size).convert("RGBA")
    gray = grayscale_img.resize(gray_size).convert("RGBA")
    
    back.alpha_composite(gray)
    #リサイズする
    new_size = (1920, 1080)
    
    cropped_image = back.crop((400,0,1520,630))
    new_size = (1920, 1080)
    box_img = cropped_image.resize(new_size)

    return box_img.convert("RGBA")

#DLしてきたbytes型の画像データをPIL.Imageに変換する
def get_img(URL):
    response = requests.get(URL)
    bytes_io = BytesIO(response.content)
    image = Image.open(bytes_io)
    return image.convert("RGBA")
   
def set_image_alpha(box_img:Image.Image,alpha:float):
    alpha = alpha
    if box_img.mode in ('RGBA', 'LA') or (box_img.mode == 'P' and 'transparency' in box_img.info):
        alpha_img = box_img.convert('RGBA')
        alpha_data = alpha_img.getdata()
        new_data = []
        for pixel in alpha_data:
            if pixel[3] == 0:
                new_data.append(pixel)
            else:
                new_pixel = (pixel[0], pixel[1], pixel[2], int(255 * alpha))
                new_data.append(new_pixel)
        alpha_img.putdata(new_data)
        box_img = alpha_img
    else:
        box_img.putalpha(int(255 * alpha))

    return box_img

