import socket
import cv2
import base64
import numpy as np

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(('localhost' , 8778))
server.listen()

conn , addr = server.accept()

OPENCV_VIDEOIO_PRIORITY_MSMF = 0

while True:
	data = conn.recv(2048000000)
	raw_image = base64.b64decode(data)
	image = np.frombuffer(raw_image, dtype=np.uint8)
	frame = cv2.imdecode(image, 1)
	cv2.imshow("frame", frame)
	cv2.waitKey(1)
	del data