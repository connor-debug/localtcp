from socket import *

client_name = "Bob"
server_name, server_port = 'localhost' , 12000

c_soc = socket(AF_INET, SOCK_STREAM)
c_soc.connect((server_name, server_port))

print("Connected to server as client: "+client_name)

inp = input("Enter an integer from 1 to 100\n")

c_soc.send((client_name + inp).encode())

print("Waiting for response now..\n")

resp = c_soc.recv(1024)
print("Response:", resp.decode())
c_soc.close()
