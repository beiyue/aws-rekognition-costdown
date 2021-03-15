import json 
import boto3 
import logging 
import json 
import base64 
import cgi 
import json 
from io import BytesIO 
import uuid
import os
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('rekognition')

path = sys.argv[1]
images = []
imagefile = []

#存储所有图片文件名称
for root, dirs, files in os.walk(path):
	for f in files:
		images.append(f)

jsonstr=''
for i in range(len(images)):
	print(images[i])
	tmpf = open(path+'/'+images[i], "rb")
	response = client.detect_labels(Image={'Bytes':tmpf.read()},MaxLabels=5,MinConfidence=99)
	for obj in response['Labels']:
		if obj['Name'] == 'Person':
			jsonstr = json.dumps(obj)
	print(jsonstr+'\n')


