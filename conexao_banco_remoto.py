import mysql.connector
import sshtunnel

sshtunnel.SSH_TIMEOUT = 10.0
sshtunnel.TUNNEL_TIMEOUT = 10.0

with sshtunnel.SSHTunnelForwarder(
		('ssh.pythonanywhere.com'),
		ssh_username='lenildojunior', ssh_password='*chicoADM*',
		remote_bind_address=('lenildojunior.mysql.pythonanywhere-services.com', 3306)
) as tunnel:
	connection = mysql.connector.connect(
  	user='lenildojunior', password='mysqlAdmin',
		host='127.0.0.1', port=tunnel.local_bind_port,
		database='lenildojunior$frutas',
	)
  # Do stuff
	cur = connection.cursor()
	query = "INSERT INTO frutas values(3,'Morango')"
	cur.execute(query)
	connection.commit()
	cur.execute("SELECT * from frutas")

	for fruta in cur:
		print("%s",fruta)		
	connection.close()
