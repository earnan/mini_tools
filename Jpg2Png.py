# 图片格式转换, Jpg转Png


from cv2 import imread, imwrite
from PIL import Image
# 方法①
img = Image.open('F:/test.png')
img.save('F:/test1.jpg')


# 方法②

image = imread("F:/test.png", 1)
imwrite("F:/test2.jpg", image)
