# -*- coding: utf-8 -*-
import socket
import numpy as np
HOST = '127.0.0.1'
PORT = 8000
expected = 0
get_first = 0

num_pkt = 10
pkt_loss = np.zeros((num_pkt, 1))

pkt_loss[4] = 1
pkt_loss[9] = 1

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

while True:
    clientMessage, addr = server.recvfrom(1024)
    if get_first == 0:
        print('Pass 1: receive packets')
        get_first = 1

    #print('Client message is:', clientMessage.decode("utf-8"))

    seq = int(clientMessage)

    if(pkt_loss[seq] == 1):
        pkt_loss[seq] = 0
        seq = -1

    if seq == expected:
        if int(clientMessage) >= 2:
            server.sendto(clientMessage, addr)
        if int(clientMessage) == 2:
            print('Pass 2: pipeline')
        if int(clientMessage) == 3:
            print('Pass 3: accumulate ack')
        expected = expected + 1
    elif seq == -1:
        print('pakcet loss')
    else:
        #print('bad packet')
        clientMessage = str(expected - 1)
        server.sendto(clientMessage.encode(), addr)

    if expected == num_pkt:
        print('Pass 4: Retransmission')
        break

