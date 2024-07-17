import cv2 
import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Dropout
from sklearn.model_selection import train_test_split


lista=[]
listap=[]

#Leitura das imagens .ppm convertidas e redimensionadas
for i in range (0,600):

    entrada = 'a' + str(i + 1) + '.ppm'
	
    img=cv2.imread('./database/converted/'+ entrada)
	#img=cv2.cvtColor(img,cv2.COLOR_RGB2YCrCb)
   
    y,cb,cr=cv2.split(img)
	#print(img.max())
    
#Definição de dados de entrada e saída da rede
    for i in range(7,57):
        for j in range(7,57):
            lista.append((y[i-7:i+8,j-7:j+8]).reshape(225))
            listap.append(cb[i,j])
   
         
#Definição de arrays para treinamento e teste
lista=np.array(lista)
lista=lista.astype(np.float32)
lista=lista/255
listap=np.array(listap)
listap=listap.astype(np.float32)
listap=listap/255
lista_treinamento,lista_teste,listap_treinamento,listap_teste=train_test_split(lista,listap,test_size=0.1)

#Criação do modelo 
regressor=Sequential()
regressor.add(Dense(units=113,activation='relu',input_dim=225))
#regressor.add(Dropout(0.2))
regressor.add(Dense(units=113,activation='relu'))
#regressor.add(Dropout(0.2))
#regressor.add(Dense(units=256,activation='relu'))
#regressor.add(Dropout(0.2))
regressor.add(Dense(units=1,activation='linear'))
regressor.compile(loss='mean_squared_error',optimizer='adam',metrics=['mean_squared_error'])
regressor.fit(lista_treinamento,listap_treinamento,batch_size=300,epochs =5,validation_data=(lista_teste,listap_teste))

#Leitura de imagem para colorir
img=cv2.imread('./for_test/s2.jpg')
img=cv2.cvtColor(img,cv2.COLOR_RGB2YCrCb)
listax=[]
#listapx=[]
y,cr,cb=cv2.split(img)
for i in range(7,660):
    for j in range(7,660):
        listax.append((y[i-7:i+8,j-7:j+8]).reshape(225))
        #vetorpx.append(cb[i,j])
        
x=np.array(listax) 
       
x=x.astype(np.float32)
x=x/255
teste=regressor.predict(x)
teste=teste*255           
teste=teste.reshape(653,653)
teste=teste.astype(np.uint8)
y=y[7:660,7:660]
cr=cr[7:660,7:660]

imgx=cv2.merge([y,cr,teste])
imgx=cv2.cvtColor(imgx,cv2.COLOR_YCrCb2RGB)
cv2.imwrite('./results/colorida2.jpg',imgx)
print('Colorida!')
