from hashlib import sha256
import time

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
            hashdata = sha256((str(self.timeStamp) + str(self.data) + str(self.previousHash) + str(self.force)).encode()).hexdigest()  #SHA256 algoritması ile bloğun tüm datasını hashliyoruz
            if hashdata[0:2] == "0x0":      #Proof of Work yani iş ispatı çift harcamayı önler.Dijital para datalardan oluşur yani kopyalanabilir.
                break                       #Bunun önüne geçmek için PoW algoritması kullanılır
        return hashdata

class Blockchain:
    def __init__(self):
        self.chain = [self.addGenesisBlock()]

    def addGenesisBlock(self):   #Genesis bloğunu oluşturma fonksiyonu
        return Block('' , time.ctime , '')  #(data , timestamp , previoushash) genesis bloğu yani doğum bloğu ilk blok olduğu için data ve previousHash bulundurmaz.

    def addBlock(self,data):   #Eklenecek blokların fonksiyonu
        node = Block(data , time.ctime() , self.chain[-1].hash) #(data , timestamp , previoushash)
        self.chain.append(node)

    def control(self):
        for i in range(len(self.chain)):
            if i != 0: # genesis bloğunu atla
                firstHash = self.chain[i-1].hash #önceki bloğun hash'i
                currentHash = self.chain[i].previousHash #şuanki previoushash
                if firstHash != currentHash: #önceki bloğun hash'i ile şuanki bloğun previousHash'i eşit olmak zorunda
                    return "error!"
                if self.chain[i].hash != sha256((str(self.chain[i].data) + str(self.chain[i].timeStamp) + str(self.chain[i].previousHash) + str(self.chain[i].force)).encode()).hexdigest():
                    return "error!"
        return "worked!"
#____________Kodun bundan sonrası kullanıcıya gösterilecek arayüzün yazılması.Bunun için form uygulaması da kullanılabilir.Terminale de çıktı verebiliriz____________
    def showBlock(self):
        for i in range(len(self.chain)):
            print("<------CoinName------>")
            print("Block=",i,"\nData=",str(self.chain[i].data),"\nTimeStamp=",str(self.chain[i].timeStamp),"\nHash=",str(self.chain[i].hash),"\nPrevious Hash =",str(self.chain[i].previousHash))
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
