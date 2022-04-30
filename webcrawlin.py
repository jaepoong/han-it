import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utils import crawling_tool
import csv

urls=crawling_tool.find_href(crawling_tool.get_content("http://www.nlic.go.kr/nlic/newspaperLi.action"))
print(urls)
crawling_tool.write_to_csv(urls,file_path="./utils/result/crawling.txt")
#driver = webdriver.Chrome(ChromeDriverManager().install())
#url='https://google.com'

#driver.get(url)
#print(driver.current_url)