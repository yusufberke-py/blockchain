from hashlib import sha256
import time
import sqlite3



class Block:
    def __init__(self,data,timeStamp,previousHash=''):
        self.data = data
        self.timeStamp = timeStamp
        self.previousHash = previousHash
        self.force = 0
        self.hash = self.createhash()
        
    
    def createhash(self):
        while True:
            self.force = self.force + 1
            hashdata = sha256((str(self.timeStamp) + str(self.data) + str(self.previousHash) + str(self.force)).encode()).hexdigest()
            if hashdata[0:2] == "00":
                break
        return hashdata

class Blockchain:
    def __init__(self):
        self.chain = [self.addGenesisBlock()]  #veritabanına şey et

    def addGenesisBlock(self):
        return Block('' , time.ctime , '')  #(data , timestamp , previoushash) genesis'de data ve previoushash yok

    def addBlock(self,data):
        node = Block(data , time.ctime() , self.chain[-1].hash) #(data , timestamp , previoushash)
        self.chain.append(node)

    def control(self): # çalışmıyo daha sonra kontrol et
        for i in range(len(self.chain)):
            if i != 0: # genesis bloğunu atla
                firstHash = self.chain[i-1].hash #ilk bloğun hash'i  
                currentHash = self.chain[i].previousHash #şuanki hash
                if firstHash != currentHash:
                    return "error!"
                if self.chain[i].hash != sha256((str(self.chain[i].data) + str(self.chain[i].timeStamp) + str(self.chain[i].previousHash) + str(self.chain[i].force)).encode()).hexdigest():
                    return "error!"
        return "worked!"
    
    def showBlock(self):
        for i in range(len(self.chain)):
            print("<------CoinName------>")
            print("Block =", i , "\nData=" , str(self.chain[i].data) , "\nTimeStamp=" , str(self.chain[i].timeStamp) , "\nHash=" , str(self.chain[i].hash) , "\nPrevious Hash =" , str(self.chain[i].previousHash))
            print("<------CoinName------>")
Coin = Blockchain()

while True:
    print("For add block:1 \nFor show blockchain:2 \nFor blockchain control:3 \nFor exit:4")
    choice = input()
    if choice == "1":
        print("Amount sent:")
        sent = input()
        Coin.addBlock(sent)
    elif choice == "2":
        Coin.showBlock()
    elif choice == "3":
        Coin.control()
    elif choice == "4":
        break
    else:
        print("wrong operation")
