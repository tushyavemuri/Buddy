#!/usr/bin/env python
# -*- coding: cp1252 -*-

import socket
import time
import logging


def buddyRequest(HOST,PORT,request,elapsedTimes,startTimes,endTimes):
    buddy = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    buddy.connect((HOST,PORT))

    startTime = time.time()
    startTimes.append(startTime)

    buddy.send(request.encode())
    response = buddy.recv(10000).decode('utf-8')

    endTime = time.time()
    endTimes.append(endTime)
    elapsedTime = endTime - startTime
    logging.info("request took {:.3f} seconds".format(elapsedTime))

    print("#--------------------------------------------------------------------------------------------------------#")
    print("")
    print(f"{response}")
    print("")
    print("#--------------------------------------------------------------------------------------------------------#")
    buddy.close()

    elapsedTimes.append(elapsedTime)

    return response
