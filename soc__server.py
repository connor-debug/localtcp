from socket import *
import random

port = 12000
s_soc = socket(AF_INET, SOCK_STREAM)
s_soc.bind(('localhost', port))
s_soc.listen(1)
ServerName = "Connor's Server"
print(ServerName + " is now online")

while True:

    con, addr = s_soc.accept()
    data = con.recv(1024).decode()

    name = ""
    valueint= ""

    for i in range( len(data)): #parsing data into int value and client name
        if data[i].isalpha():
                name = name + data[i]
        else:
                valueint = valueint + data[i]

    rint = random.randint(1,100)
    print("Selected random number: "+str(rint))

    value_resp = int(valueint) + int(rint)
    client_resp = ServerName+ " choose number " + str(rint)+",now responding to client " + name +": "

    full_resp = client_resp + str(value_resp)

    
    con.send((str(full_resp)).encode())
    print("Reply sent")
    con.close()
