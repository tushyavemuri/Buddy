#!/usr/bin/env python
# -*- coding: cp1252 -*-

import socket
import time
import logging


def buddyRequest(HOST,PORT,request,elapsedTimes):
    buddy = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    buddy.connect((HOST,PORT))

    startTime = time.time()

    buddy.send(request.encode())
    response = buddy.recv(1024).decode('utf-8')

    endTime = time.time()
    elapsedTime = endTime - startTime
    logging.info("request took {:.3f} seconds".format(elapsedTime))

    buddy.close()

    elapsedTimes.append(elapsedTime)

    return response