#!/usr/bin/python
# coding=utf-8

import socket,traceback

HOST = "10.1.1.144"
PORT = 8888

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#可以重复使用端口号

s.bind((HOST,PORT))

s.listen(1)

while True:
    try:
        clientsock,clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    clientsock.settimeout(5)

    try:
        print "Got connection from:",clientsock.getpeername()
        while True:
            data = clientsock.recv(4096)
            if not len(data):
                break
            clientsock.sendall(data)

    except (KeyboardInterrupt,SystemExit):
        raise
    except socket.timeout:
        print 'timeout...............'
    except:
        traceback.print_exc()

    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()