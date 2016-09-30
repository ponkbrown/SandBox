import requests, goslate
from bs4 import BeautifulSoup

sitio = 'https://daringtolivefully.com/journal-prompts'

r = requests.get(sitio)
html = r.content

#with open('file.html', 'r') as f:
#    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

titulos = soup.findAll('h2',attrs={'class':None})

for h2 in titulos:
    if h2.find_next('ul'):
#        import pdb; pdb.set_trace()
        print('{0}:\n\t{1}'.format(h2.text, h2.find_next('ul').text))
        input()
