from bs4 import BeautifulSoup
import requests
import csv

def fazer_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def pegar_link(soup):
    try:
        link = soup.find_all('a', {'class': 's-item__link'})
    except:
        link = 'null'

    urls = [i.get('href') for i in link]
    return urls
    
def info_produto(soup):
    try:
        titulo = soup.find('span', {'class':'ux-textspans ux-textspans--BOLD'}).text
    except:
        titulo = ''
    try:
        preco = soup.find('span', {'class':'ux-textspans ux-textspans--SECONDARY ux-textspans--BOLD'}).text
    except:
        preco = 'null'

    data = {
        'titulo' : titulo,
        'preco' : preco }

    return data

def guardar_info(data, url):
    with open ('Dados dos produtos.csv', 'a', encoding='utf-8') as arq:
        escrever = csv.writer(arq)
        row = [data['titulo'],data['preco'], url]
        escrever.writerow(row)


def main():
    url = 'https://www.ebay.com/sch/i.html?_nkw=relogio&_sacat=0&_from=R40&_pgn=1'
    produtos = pegar_link(fazer_request(url))
    for i in produtos:
        data = info_produto(fazer_request(i))
        guardar_info(data, i)

if __name__ == '__main__':
    main()

