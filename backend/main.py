
import newspaper
import requests
import pandas as pd 
import json

from bs4 import BeautifulSoup

HACKERNEWS_API = 'https://hacker-news.firebaseio.com/v0/'

def get_hn_stories(kind='best', limit=10):
    url = HACKERNEWS_API + kind + 'stories.json'
    r = requests.get(url)
    return r.json()[0:limit]


def get_hn_item(item_id):
    url = HACKERNEWS_API + 'item/' + str(item_id) + '.json'
    r = requests.get(url)
    return r.json()


def hackernews_rss(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.findAll('item')
        for article in  process_hn_items(articles):
            print(article)
    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)
    return r.status_code


def process_hn_items(articles):
    article_list = []           
    for a in articles:
        title = a.find('title').text
        item_id = extract_item_id(a.find('comments').text)
        link = a.find('link').text
        published = a.find('pubDate').text            
        article = {
            'title': title,
            'link': link,
            'published': published,
            'item_id': item_id
        }
        article_list.append(article)
    return article_list


def extract_item_id(comment_url):
    digits = [d for d in comment_url if d.isdigit()]
    return ''.join(digits)
        

def scrape_hn_rss():
    print('Starting scraping')

    url = 'https://news.ycombinator.com/rss'
    status_code = hackernews_rss(url)

    if status_code == 200:
        print('Finished scraping')
    else:
        print('Something went wrong with the scraping.')


def article_processor(url):
    article = newspaper.Article(url)
    article.build()
    return [article.summary, article.keywords, article.top_image]


def get_hn_stories_json():
    item_list = []
    for item_id in get_hn_stories():
        print("Processing : " + str(item_id))
        json = get_hn_item(item_id)
        summary, keywords, image = article_processor(json['url'])
        json['summary'] = summary
        json['keywords'] = keywords
        json['image'] = image
        item_list.append(json)
    return item_list

if __name__ == '__main__':
    df = pd.DataFrame(get_hn_stories_json(), columns=['by', 'descendants', 'id', 'kids', 'score', 'time', 'title', 'type', 'url', 'summary', 'keywords', 'image'])
    print(df.head())





    
    
    
    
