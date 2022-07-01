from http import server
import socket
import time

HOST = '127.0.0.1'
PORT = 8000
server_addr = (HOST, PORT)

send_base = 0 
next_seq_num = 0

cwnd_size = 3
num_pkt = 10

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# TODO: write your codes here
while next_seq_num<num_pkt:
    while(next_seq_num - send_base)<cwnd_size:
        outdata = str(next_seq_num)
        client.sendto(outdata.encode(), server_addr)
        next_seq_num+=1

    indata=''
    client.settimeout(5)
    try:
        indata, addr = client.recvfrom(1024)
    except Exception as e:
        #print("timeout")
        next_seq_num = send_base 
    
    if len(indata) > 0:
        send_base = int(indata)+1
        
num = 1
while next_seq_num>send_base:
    try:
        indata, addr = client.recvfrom(1024)
        num+=1
        if num == cwnd_size:
            break
    except Exception as e:
        for i in range(send_base,next_seq_num):
            clientMessage = str(i)
            client.sendto(clientMessage.encode(),server_addr)