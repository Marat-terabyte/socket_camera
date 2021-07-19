import socket 
import cv2
import base64
import numpy as np

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(('localhost' , 554))

while True:
	data = client.recv(1228800000)
	
	raw_image = base64.b64decode(data)
	image = np.frombuffer(raw_image, dtype=np.uint8)
	frame = cv2.imdecode(image, 1)
	
	cv2.imshow("camera", frame)
	cv2.waitKey(1)
	del data