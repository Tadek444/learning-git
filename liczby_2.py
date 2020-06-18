lista=[]
lista_q=[]
for i in range (1,101):    
    if i%5==0:
        (lista.append(i))
        (lista_q.append(i**3))
print('Liczby co 5')
print (lista)    
print ('Liczby sześcienne')
print (lista_q)