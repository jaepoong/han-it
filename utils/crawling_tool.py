import os
from urllib.error import HTTPError
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

def get_content(url):
    # 현재 페이지의 가사 링크 주기.
    try:
        res=requests.get(url)
    except HTTPError as e:
        return None
    return res.content

def find_href(content):
    # content에 있는 링크 반납.
    title=content.find("div",class_="board_list")
    wr=title.find_all("ul",class_="wr_field")
    href_list=[]
    for w in wr:
        href_list.append(w.find("a")["href"])
    return href_list

def get_data(url):
    soup=BeautifulSoup(get_content(url),"html.parser")
    head=soup.find("h3",class_="heading").get_text()
    subhead=soup.find("h4",class_="subheading").get_text()
    contents=soup.find("div",class_="article-body")
    contents=soup.find_all("p")
    con=""
    for content in contents:
        con+=str(content.get_text())
    con=con[:-2]
    data=[head,subhead,con]
    return data

ㅇㄷㄹ