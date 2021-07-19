import socket
import cv2
import base64
import threading

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(('localhost' , 554))
server.listen()

cap = cv2.VideoCapture(0 , cv2.CAP_DSHOW)


def camera(conn):
	while True:
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
		encoded, buf = cv2.imencode('.jpg', frame)


		image = base64.b64encode(buf)

		conn.send(image)


def start_server():	
	conn , addres = server.accept()
	
	camera_threading = threading.Thread(
		target = camera,
		args = (conn,)
		)

	camera_threading.start()


if __name__ == '__main__':
	start_server()


'''
while True:
	conn , addres = server.accept()
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	encoded, buf = cv2.imencode('.jpg', frame)
	image = base64.b64encode(buf)
	conn.send(image)

cap.release()
cv2.destroyAllWindows()'''