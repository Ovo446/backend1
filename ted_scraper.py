import requests                               # 用于发送网页请求
from bs4 import BeautifulSoup                 # 用于解析 HTML 网页内容

def get_ted_talks():                          # 定义函数，用于爬 TED 演讲
    url = 'https://www.ted.com/talks'         # TED 演讲页面的网址
    response = requests.get(url)              # 向网址发 GET 请求
    soup = BeautifulSoup(response.text, 'html.parser')  # 用 html.parser 解析网页
    titles = [a.text.strip() for a in soup.select('div.talk-link a.ga-link')[:5]]  # 抓前5个演讲标题
    return {'talks': titles}                  # 返回结果作为 JSON 字典
