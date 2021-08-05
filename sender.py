import bitarray
import pickle
import socket
import random

def verification(message):
  hexmessage = message.encode('ascii')
  bitarr = bitarray.bitarray()
  bitarr.frombytes(hexmessage)
  return bitarr

def noise(bitarr, prob):
  newBitArr = bitarray.bitarray(len(bitarr))
  for i in range(len(bitarr)):
    if random.random() < prob:
      newBitArr[i] = not bitarr[i]
    else:
      newBitArr[i] = bitarr[i]
  return newBitArr

def transmission(bitarr, serverName, serverPort):
  pickleString = pickle.dumps(bitarr)
  clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  clientSocket.sendto(pickleString, (serverName, serverPort))
  clientSocket.close()


#capa de aplicacion

server = 'localhost'
port = 12000
message = "hola que tal como estas?"
noiseProb = 1/4

#capa de verification
ba = verification(message)
#capa de ruido
noisedBa = noise(ba, noiseProb)

'''print("Before:", ba)
print("After:", noisedBa)
print("Difference:", (ba^noisedBa).count(1))'''

#transmission
transmission(ba, server, port)
