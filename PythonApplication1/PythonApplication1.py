from asyncio import sleep
import random
from turtle import delay
matris = 10
sayi = int()
x = int()
y = int()
kap = list()

class Pire:
   
    def __init__(self):#oluþturma

        self.kordX = random.randint(0, matris-1)
        self.kordY = random.randint(0, matris-1)
    
    
    def move(self):#hareket metodu
        drec = random.randint(0, 1)
        if drec  == 0 :
            if self.kordX < matris-1:
               self.kordX +=1
            elif self.kordX == matris-1:
                self.kordX -=1

        if drec == 1 :
            if 0 < self.kordX:
                self.kordX -=1
            elif 0 == self.kordX:
                self.kordX +=1

        if drec == 2 :
            if self.kordY < matris-11:
                self.kordY +=1 
            elif 0 == self.kordY :
                self.kordY -=1
        if drec == 3 :
            if 0 < self.kordY:
                self.kordY -=1
            elif 0 == self.kordY :
                self.kordY +=1
            


for i in range(40):# x pire oluþtur
    kap.append(Pire())

for l in range(10):

    for y in range(matris):
        for x in range(matris):#matris for döngüleri
            for z in kap:#pire konum bulma
                if x == z.kordX and y == z.kordY:
                    sayi +=1
                
            print(f"{sayi:2}",end=" ")
            sayi = 0
        print()

    for z in kap:#pire hareket etirme
        z.move()

    input()
    #print()
    

print("son")