import os
import random
import sys

from PIL import Image
 
#单个图片的大小为320*240
UNIT_SIZE = 720
TARGET_WIDTH = 4 * UNIT_SIZE
 
path = sys.argv[1]

images = []
imagefile = []

#存储所有图片文件名称
for root, dirs, files in os.walk(path):
    for f in files:
        images.append(f)
        print(f)

#我这里是将4张图片横向拼接
for i in range(len(images)):
    imagefile.append(path+'/'+images[i])

left = 0
right = 0
target = Image.new('RGB',(TARGET_WIDTH, 480))

for image in imagefile:
    #print(image)
    #将现有图片复制到新的上面 参数分别为图片文件和复制的位置(左上角, 右下角)
    x,y = Image.open(image).size
    right = y
    target.paste(Image.open(image), (left, 0, (left+x), right))
    left += x
    
    #图片的质量 0~100
    quantity_value = 100
    if imagefile.index(image) % 4 == 0 or (len(imagefile) -1 == imagefile.index(image)) : 
        target.save(path+'/merge/merge'+str(random.randint(1,1000)).rjust(4,'0') +'.jpg', quantity = quantity_value)
        left = 0
        right = 0
        target = Image.new('RGB',(TARGET_WIDTH, 480))

'''
for i in range(5):
    imagefile.append(path+'/'+images[i])
    target = Image.new('RGB',(TARGET_WIDTH, UNIT_SIZE))
    left = 0
    right = UNIT_SIZE
print(imagefile)
for image in imagefile:
    #print(image)
    #将现有图片复制到新的上面 参数分别为图片文件和复制的位置(左上角, 右下角)
    target.paste(Image.open(image), (left, 0, right, UNIT_SIZE))
    left += UNIT_SIZE
    right += UNIT_SIZE
    #图片的质量 0~100
    quantity_value = 100
    target.save(path+'/end.jpg', quantity = quantity_value)
'''


