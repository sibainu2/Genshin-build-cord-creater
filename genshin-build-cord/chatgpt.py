import cv2
import numpy as np

# 画像を読み込み、グレースケールに変換する
img = cv2.imread(r'overlay.jpg', cv2.IMREAD_GRAYSCALE)

# 暗いところほど黄色みを強調するために、黄色を指定する
color = (255, 0, 0)  # BGRで指定する必要があるため、黄色は(0, 255, 255)

# カラーマップを作成する
color_map = np.zeros((256, 1, 3), dtype=np.uint8)
for i in range(256):
    color_map[i][0] = color

# カラーマップを適用し、明度を下げた画像を生成する
output = cv2.applyColorMap(img, color_map)

# 生成された画像を表示する
cv2.imshow('output', output)
cv2.waitKey(0)