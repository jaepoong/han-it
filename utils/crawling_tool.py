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
    content=BeautifulSoup(content,"html.parser")
    title=content.find("div",class_="board_list")
    wr=title.find_all("ul",class_="wr_field")
    href_list=[]
    for w in wr:
        href_list.append(w.find("a")["href"])
    return href_list


def get_data(url):
    # 해당 url데이터 모아서 
    soup=BeautifulSoup(get_content(url),"html.parser")
    try:
        head=soup.find("h3",class_="heading").get_text()
    except:
        head=None
    try:
        subhead=soup.find("h4",class_="subheading").get_text()
    except:
        subhead=None
    try:
        contents=soup.find("div",class_="article-body")
        contents=soup.find_all("p")
        con=""
        for content in contents:
            con+=str(content.get_text())
        con=con[:-2]
    except:
        con=None
    data=[head,subhead,con]
    return data


def write_to_csv(urls,file_path=None,write_type='a'):
    # url들을 받아서 정보 만들어서 저장.
    f=open(file_path,write_type)
    csvWriter=csv.writer(f)
    for url in urls:
        data=get_data(url)
        csvWriter.writerow(data)
    f.close()

        
        
        

