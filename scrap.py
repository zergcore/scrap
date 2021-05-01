from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://resultados.as.com/resultados/futbol/primera/clasificacion/'
page=requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser') #Obtener los elementos en formato html

#Equipos

eq=soup.find_all('span', class_='nombre-equipo')
#print(eq)

equipos=list()

count=0
for i in eq:
    if count < 20:
        equipos.append(i.text) #agrega el texto a la lista
    else:
        break
    count+=1 #count=count+1

#print (equipos)

#Puntos
pt=soup.find_all('td', class_='destacado') #etiqueta, clase

puntos=list()

count1=0
for i in pt:
    if count1 < 20:
        puntos.append(i.text) #agrega el texto a la lista
    else:
        break
    count1+=1 #count=count+1

#print(puntos)

df=pd.DataFrame({'Nombre' : equipos, 'Puntos' : puntos},index=list(range(1,21)))

print(df)

df.to_csv('Clasificacion.csv', index=False)




#Sacar la primera división y los puntos del diario as en un dataframe