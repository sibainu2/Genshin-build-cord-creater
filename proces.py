import cv2
import numpy as np
# 3チャンネル(BGR)画像を読み込む
img = cv2.imread(r'C:\Users\sibainu\Desktop\Genshin-bot\overlay.jpg', cv2.IMREAD_GRAYSCALE)


cv2.imshow('output', img)
cv2.waitKey(0)
# 明るさを増やす
alpha = 5
beta = 100
adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
cv2.imshow('output', adjusted)
cv2.waitKey(0)

# グレースケール画像を赤色のチャンネルに変換する
img_red = cv2.cvtColor(adjusted, cv2.COLOR_GRAY2BGR)
img_red[:, :, 0] = 0
img_red[:, :, 1] = 0

cv2.imshow('output', img_red)
cv2.waitKey(0)


# 生成された画像を表示する
cv2.imshow('output', img_red)
cv2.waitKey(0)
