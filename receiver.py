import bitarray
import pickle
import socket

port = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(("", port))
while True:
  pickleMessage, clientAddress = serverSocket.recvfrom(2048)
  bitmessage = pickle.loads(pickleMessage)
  message = bitmessage.tobytes().decode()

  if message:
    print(message)