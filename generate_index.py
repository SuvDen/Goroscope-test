# coding: utf-8

from horoscope import generate_prophecies
from datetime import datetime as dt

def generate_body(header, paragraphs):
    body = '<h1>' + header + '</h1>'
    for p in paragraphs:
        body += '<p>' + p + '</p>'
    return '<body>' + body

def generate_head(title):
   head = '<title>' + title + '</title>' 
   head += '<meta charset="utf-8">'
   return '<head>' + head + '</head>'

def generate_link(text_link):
    trait = '<hr/>' + '&nbsp;'
    link = trait + '<a href="about.html">' + text_link + '</a>' + '</body>'
    return link

def save_page():
    p = generate_prophecies()
    today = dt.now().date()
    head = generate_head(title='Гороскоп')
    body = generate_body(header="Гороскоп на " + str(today), paragraphs=p)
    link = generate_link(text_link='О реализации')
    page = head + body + link
    
    index_open = open("index.html", "w")
    print(page, file=index_open)
    index_open.close()

save_page()
