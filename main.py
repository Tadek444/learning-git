list_5=[]
list_q=[]
for i in range (1,101):    
    while i%5!=0:
        i+=1
        break
    else:
        (list_5.append(i))
        (list_q.append(i**3))
print('Liczby co 5')
print (list_5)    
print ('Liczby sześcienne')
print (list_q)
print ('to naprawdę dobry kod')
