import bitarray
import pickle
import socket

#capa de transmision
def transmission(serverPort):
  serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  serverSocket.bind(("", serverPort))
  while True:
    pickleMessage, clientAddress = serverSocket.recvfrom(2048)
    bitmessage = pickle.loads(pickleMessage)
    if bitmessage:
      return bitmessage

#capa de verificacion
def hamming():
  pass

def FletcherChecksum():
  pass

#capa de aplicación
port = 12000
bitmessage = transmission(port)
message = bitmessage.tobytes().decode()

print(message)
