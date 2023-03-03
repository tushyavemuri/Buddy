import threading
import BuddyRequest as BR




HOST = input("Enter the network address to connect to: ")

# check valid network address
# check whether we are able to ping the addess

PORT = int(input("Enter the port number to connect to: "))

# check valid port

request = input("Enter the operation to request (Date and Time, Uptime, Memory Use, Netstat, Current Users, or Running Processes): ")

# change to switcher

numOfRequests = int(input("Enter the number of client requests to generate (1, 5, 10, 15, 20, or 25): "))

# change to switcher

threads = []

for i in range(numOfRequests):
    t = threading.Thread(target=BR.buddyRequest, args=(HOST, PORT, request))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

totalTime = sum(t.result() for t in threads)
avgTime = totalTime / numOfRequests

print("Total turn-around time: {:.3f} seconds".format(totalTime))
print("Average turn-around time: {:.3f} seconds".format(avgTime))




