import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0",2222))
s.listen(1)
while True:
	client, addr = s.accept()
	while True:
		data = client.recv(1024)
		if not data: break
		client.send(data)
		if data == 'close' or data =='Close':
			client.close()
	client.close()