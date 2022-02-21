import numpy as np
import cv2


#convertendo as imagem mapa ppm e redimensionando-as

qt_imagens = 690

a=0
for a in range(690):
	
	a=a+1

	
	c=str(a)
	nome = ".jpg"
	nomes=".ppm"
	final=c+nome
	#print(final)
	img = cv2.imread('/home/matheus/Documentos/colorizer/database/original/' + final)
	#cv2.imshow("Original", img)
	img=cv2.cvtColor(img,cv2.COLOR_RGB2YCrCb)
	#y = img[:,:,0]; 
    
	#m = y[1:10,1:10]
	#print(m)
	#print(img.shape)
	
	#RGB=cv2.cvtColor(img,cv2.COLOR_YCrCb2RGB)
	largura = img.shape[1]
	altura = img.shape[0]
	proporcao = float(altura/largura)
	largura_nova = 70 #em pixels
	#altura_nova = int(largura_nova*proporcao)
	altura_nova=70
	tamanho_novo = (largura_nova, altura_nova)
	img_redimensionada = cv2.resize(img,
	tamanho_novo, interpolation = cv2.INTER_AREA)
	#cv2.imshow('Resultado', img_redimensionada)
	#cv2.waitKey(0)
	saida="a"
	final=saida+c+nomes
	#print(final)
	cv2.imwrite('/home/matheus/Documentos/colorizer/database/converted/' + final, img_redimensionada)
	#cv2.imshow("test", y)
	#cv2.waitKey(0)


print('Conversão finalizada!')