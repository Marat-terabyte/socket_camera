import socket
import cv2
import nmap
import base64

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(('localhost' , 8778))

cap = cv2.VideoCapture(0)
OPENCV_VIDEOIO_PRIORITY_MSMF = 0



while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	encoded, buf = cv2.imencode('.jpg', frame)
	image = base64.b64encode(buf)
	client.send(image)


cap.release()
cv2.destroyAllWindows()