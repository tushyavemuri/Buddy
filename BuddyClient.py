#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import threading
import buddyrequest as BR
import logging
import logging.config

def main():
    # Logger settings
    logging.config.fileConfig("budlog.conf")
    logging.getLogger('buddyFileLogger')


    #HOST = input("Enter the network address to connect to: ")
    HOST = '127.0.0.1'
    # check valid network address
    # check whether we are able to ping the addess

    #PORT = int(input("Enter the port number to connect to: "))
    PORT = 55777

    # check valid port

    request = input("Enter the operation to request (Date, Uptime, Memory, Network, Users, or Processes): ")
    #request = 'date'
    # change to switcher

    #numOfRequests = int(input("Enter the number of client requests to generate (1, 5, 10, 15, 20, or 25): "))
    numOfRequests = 5
    # change to switcher

    elapsedTimes = []
    threads = []

    for i in range(numOfRequests):s
        t = threading.Thread(target=BR.buddyRequest, args=(HOST, PORT, request,elapsedTimes))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    totalTime = sum(elapsedTimes)
    avgTime = totalTime / numOfRequests

    logging.info("Total turn-around time: {:.3f} seconds".format(totalTime))
    logging.info("Average turn-around time: {:.3f} seconds".format(avgTime))


if __name__ == "__main__":
  main()

