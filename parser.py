import requests
from bs4 import BeautifulSoup


def get_collection(url: str) -> str:
    response = requests.get(f'{url}category/product')
    new_blog = 0
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.findAll('a'):
        blog = link.get('href')
        if '/blog/' in blog:
            new_blog = link.get('href')
            break
    return f'{url}{new_blog}'


def get_blog(url: str) -> dict:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image = soup.find('div', 'collection-item-4').find('img').attrs['src']
    news_text = soup.find('a', 'blog-hero-heading').text.upper() + '\n\n'
    for paragraph in soup.find('div', 'blog-post-content'):
        text = paragraph.text
        if not text:
            pass
        else:
            if 'â' in text:
                text = text.replace('â', '-')
            if '' in text:
                text = text.replace('', "'")
            if '' in text:
                text = text.replace('', '"')
            if '' in text:
                text = text.replace('', '"')
            if 'Â' in text:
                text = text.replace('Â', '')
            if 'â' in text:
                text = text.replace('â', '')
            news_text += text + '\n\n'
    return {'media': image, 'text': news_text}