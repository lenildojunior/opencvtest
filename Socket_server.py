import socket

HOST = socket.gethostbyname(socket.gethostname())  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	while True:
		print("Aguardando conexão no endereço:", HOST," na porta: ",PORT)
		conn, addr = s.accept()
		with conn:
			print('Connected by', addr)
			data = conn.recv(1024)
			print (data)
			conn.sendall(data)