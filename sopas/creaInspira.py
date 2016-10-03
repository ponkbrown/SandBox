import requests, goslate
from bs4 import BeautifulSoup
import json

# Esto es cuando hay internet
# sitio = 'https://daringtolivefully.com/journal-prompts'
# r = requests.get(sitio)
# html = r.content


with open('file.html', 'r') as f:
    html = f.read()

gs = goslate.Goslate(a)

soup = BeautifulSoup(html, 'html.parser')
titulos = soup.findAll('h2',attrs={'class':None})
titulos = titulos[:-2]

inspire = {}

for titulo in titulos:
    lista = []
    lis = titulo.find_next('ul').find_all('li')
    for li in lis:
        lista.append(li.get_text().strip())
    inspire[titulo.get_text().strip()] = lista

for titulo in inspire:
    lista = []
    for li in inspire[titulo]:
        lista.append(gs.translate(li, 'es'))
    inspira[gs.translate(titulo,'es')] = lista

with open('inspire.json', 'w') as f:
    f.write(json.dumps(inspire, sort_keys = True, indent = 2))
with open('inspira.json', 'w') as f:
    f.write(json.dumps(inspira, sort_keys=True, indent = 2))
