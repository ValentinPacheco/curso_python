'''prueba de BeautifullSoup'''
from bs4 import BeautifulSoup

html = "<html><head><title>Test</title></head><body><h1>Hola Mundo</h1></body></html>"
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())
print(soup.h1.text)
soup.p.string = "Hola Mundo"
soup.h1.string = "Hola Mundo de soup"
nueva_etiqueta = soup.new_tag("p")
nueva_etiqueta.string = "soy una nueva etiqueta"
soup.body.append(nueva_etiqueta)
nueva_liga = soup.new_tag("a", href="https://www.google.com")
nueva_liga.string = "Google"
soup.body.append(nueva_liga)
print(soup.prettify())
print("--------------------")
print(soup.find("h1"))
print(soup.find_all("p"))
parrafos = soup.find_all("p")
lista_parrafos = []
for p in parrafos:
    lista_parrafos.append(p.string)
print(lista_parrafos)
print("--------------------")