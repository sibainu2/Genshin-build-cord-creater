from PIL import Image, ImageDraw
import numpy as np
from PIL import Image

# 画像を読み込む
img = Image.open(r"data\chara_img\banner_Nilou.png")


img = img.crop((650,100,1400,800))
# 画像をRGBAモードに変換する
img = img.convert("RGBA")
x,y = img.size
# 画像のピクセルデータをNumPy配列に変換する
pixels = np.array(img)

# 2列目のピクセルの不透明度を0.5倍に変更する
opacity =  1
a=0
for h in range(1,x):
  print(x-h<=300 )
  print(1/x*a)
  if x-h<=50:
    pixels[:, h, 3] = (pixels[:, h, 3] *(opacity-(1/x*a*10))).astype(np.uint8)
    a+=1.5

# 変更後のピクセルデータを元の形式に変換する
imga = Image.fromarray(pixels)

# 変更後の画像を保存する
imga.show()
