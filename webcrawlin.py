import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utils import crawling_tool
import csv
soup=BeautifulSoup(crawling_tool.get_content("http://www.shippingnewsnet.com/news/articleView.html?idxno=47412"),"html.parser")



f = open('utils/result/crawling.txt','a')
f.write("hellow ")
f.close()

print(crawling_tool.get_data("http://www.shippingnewsnet.com/news/articleView.html?idxno=47412"))
#driver = webdriver.Chrome(ChromeDriverManager().install())
#url='https://google.com'

#driver.get(url)
#print(driver.current_url)