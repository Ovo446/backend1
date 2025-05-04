# ted_scraper.py
import requests
from bs4 import BeautifulSoup

def get_ted_talks():
    url = "https://www.ted.com/talks"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    titles = [tag.text.strip() for tag in soup.select("h4.h9")]
    return {"talks": titles[:10]}  # 返回前10个演讲标题
