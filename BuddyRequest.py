import socket
import time


def buddyRequest(HOST,PORT,request,elapsedTimes):
    buddy = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    buddy.connect((HOST,PORT))

    startTime = time.time()

    buddy.send(request.encode())
    response = buddy.recv(1024)

    endTime = time.time()
    elapsedTime = endTime - startTime
    #print("request took {:.3f} seconds".format(elapsedTime))

    buddy.close()

    elapsedTimes.append(elapsedTime)