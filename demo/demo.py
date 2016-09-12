#! /usr/bin/env python

# encoding=utf-8

import requests
from bs4 import BeautifulSoup
import codecs

DOWN_LOAD = 'https://movie.douban.com/top250'

def download_page(url):
    data = requests.get(url).content
    return data

def main():
    url = DOWN_LOAD

    with codecs.open('movies','wb', encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            movies, url = parse_html(html)
            fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))

def parse_html(html):
    soup = BeautifulSoup(html,'html.parser')

    move_list_soup = soup.find('ol',attrs={'class':'grid_view'})

    movie_list = []

    for move_li in move_list_soup.find_all('li'):

        detail = move_li.find('div', attrs={'class':'hd'})
        movie_name = detail.find('span', attrs={'class':'title'}).getText()
        movie_list.append(movie_name)
    
    next_page = soup.find('span',attrs={'class':'next'}).find('a')
    if next_page:
        return movie_list, DOWN_LOAD + next_page['href']
    return movie_list, None
        

if __name__ == '__main__':
  main()
