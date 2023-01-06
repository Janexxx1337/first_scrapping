from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')
top_articles = soup.select(selector='.titleline a')

score = soup.select(selector='.subline .score')

score_list = []

for key in score:
    score_list.append(key.getText())

only_num = []
for score in score_list:
    only_num.append(int(score.split()[0]))

articles = []
articles_link = []

for article in top_articles:
    articles.append(article.getText())
    articles_link.append(article.get('href'))

largest = max(only_num)

print(largest)
largest_index = only_num.index(largest)

print(articles[largest_index])
print(articles_link[largest_index])


print(articles)
