from bs4 import BeautifulSoup as BS
import requests  
import pandas as pd 
from bs4 import BeautifulSoup
import requests
import csv
import time
import os

url_list = ['https://www.bankbazaar.com/reviews.html?reviewPageNumber=1',
'https://www.bankbazaar.com/reviews.html?reviewPageNumber=2',
'https://www.bankbazaar.com/reviews.html?reviewPageNumber=3',
'https://www.bankbazaar.com/reviews.html?reviewPageNumber=4', 
'https://www.bankbazaar.com/reviews.html?reviewPageNumber=5', 
'https://www.bankbazaar.com/reviews.html?reviewPageNumber=6']

reviews=[]
user_names=[]


for link in url_list:
    r = requests.get(link)
    r.encoding = 'utf-8'
    html_content = r.text
    soup=BS(html_content,'html.parser')
    for jobs in soup.find_all('li',{'class':'review-box'}):
        review=jobs.find('div',{'class':'text_here review-desc-more'}).text.strip()
        user_name=jobs.find('a',{'class':'user-review-comment js-individual-title'}).text.strip()
        reviews.append(review)
        user_names.append(user_name)
        list_of_tuples = list(zip(reviews, user_names))
        df = pd.DataFrame(list_of_tuples, columns = ['Reviews', 'User_Names']
        
        
        

