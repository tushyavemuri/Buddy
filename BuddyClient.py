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


    HOST = input("Enter the network address to connect to: ")
    #HOST = '139.62.210.155'
    # check valid network address
    # check whether we are able to ping the addess

    PORT = int(input("Enter the port number to connect to: "))
    #PORT = 3333

    while True:
        # check valid port
        print("""
        1. Date and Time
        2. Uptime
        3. Memory
        4. Network stats
        5. Current Users
        6. Running Processes
        7. Exit

        Select the required information about Host {HOST} from above options.
        """)

        selection = int(input(""))

        if selection not in [1,2,3,4,5,6,7]:
            print("Invalid request")
            continue

        inputmap = {1:"date",
        2:"uptime",
        3:"memory",
        4:"network",
        5:"users",
        6:"processes" 
        }

        if selection == 7:
            print("Good bye!")
            break

        request = inputmap[int(selection)]


        # change to switcher

        numOfRequests = int(input("Enter the number of client requests to generate (1, 5, 10, 15, 20, or 25): "))
        # numOfRequests = 5
        # change to switcher

        elapsedTimes = []
        threads = []

        for i in range(numOfRequests):
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

