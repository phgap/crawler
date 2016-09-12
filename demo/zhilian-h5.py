#! /usr/bin/env python
# encoding=utf-8

import requests

import Queue

from bs4 import BeautifulSoup

initial_page = 'http://sou.zhaopin.com/jobs/searchresult.ashx?bj=160000&sj=044%3B045%3B079%3B667%3B053&in=210500%3B160400%3B160000%3B160600%3B180000%3B180100%3B300500&pd=7&jl=%E5%A4%A7%E8%BF%9E&kw=html5&sm=0&p=1'

url_queue = Queue.Queue()

seen = set()

# seen.insert(initial_pate)
url_queue.put(initial_page)


def download_page(url):
    content = requests.get(url).content
    # print content
    return content 
    
    

def parse_page(content):
    soup = BeautifulSoup(content, 'html.parser');
    next_page = soup.find('a', attrs={'class':'next-page'})
    class_attr = next_page['class']
    # get next page>>>>>>>>>>>
    if len(class_attr) < 2:
        print next_page['href']
        url_queue.put(next_page['href'])

    #get job info >>>>>>>>>>>>>

while(True):
    if not url_queue.empty():
        current_url = url_queue.get()
        content = download_page(current_url)
        parse_page(content)
    else:
        break
        #store()
