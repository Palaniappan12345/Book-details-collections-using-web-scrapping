from bs4 import BeautifulSoup
import requests
import pandas as pd

names = []
authors = []
ratings = []
prices = []
url='https://www.flipkart.com/search?q=machine+learning&sid=bks&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_na&as-pos=1&as-type=RECENT&suggestionId=machine+learning%7CBooks&requestId=5fb8b535-c100-4782-bcbe-16131e2dd556&as-searchtext=machine%20learnin'

response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

scraping_part = soup.findAll("div",class_="_1HmYoV _35HD7C")
for s in scraping_part:
    content = s.findAll("div",class_="_3O0U0u")
    for c in content:
        inner_content = c.findAll("div",class_="_3liAhj")
        for i in inner_content:
            name = i.find("a",class_="_2cLu-l").text
            author_content = i.find("div",class_ = "_1rcHFq").text
            author = author_content.split(',')[2]
            
            rating = i.find("div",class_ = "hGSR34")
            if(rating is not None):
                rating = rating.text
            
               # print("rating:no rating given")
            price = i.find("div",class_ = "_1vC4OE").text
           # print("============================================")
            names.append(name)
            authors.append(author)
            ratings.append(rating)
            prices.append(price)
df = pd.DataFrame({'Product Name':names,'Author Name':authors,'Rating':ratings,'Price':prices}) 
df.to_csv('product.csv', index=False, encoding='utf-8')