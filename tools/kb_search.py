import os
import sys
import requests
from parsel import Selector
from urllib.parse import urljoin

COOKIE = """
fp=62a05783fe2dc24080ef6aeb0010ea38; deepinid_login=UT_him6qt8w1f7er019656x0bk311ili; mmwikipassport=mfebmfrJi4aSize1uEgFhwmEgzaDi49AiArHizsQgzWcidhQiAhzizaJgzQ=; mmwikissid=d7c81922c085c104f029ef75ca527b46
""".strip()
# COOKIE_FILE = os.path.join(os.path.dirname(__file__), 'kb_cookie')

def get_cookie(cookie_file) -> str:
    with open(cookie_file, 'r', encoding="utf8") as f:
        return f.read().strip()


def get_resp(keyword):
    headers = {
        'authority': 'kb.uniontech.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        # 'cookie': 'fp=62a05783fe2dc24080ef6aeb0010ea38; deepinid_login=UT_him6qt8w1f7er019656x0bk311ili; mmwikipassport=mfebmfrJi4aSize1uEgFhwmEgzaDi49AiArHizsQgzWcidhQiAhzizaJgzQ=; mmwikissid=d7c81922c085c104f029ef75ca527b46',
        'referer': 'https://kb.uniontech.com/main/search',
        'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57',
    }

    headers.update({"cookie": COOKIE})
    params = (
        ('search_type', 'title'),
        ('keyword', keyword),
    )
    resp = requests.get('https://kb.uniontech.com/main/search', headers=headers, params=params)
    return resp


def filter_ret(response, word):
    selector = Selector(text=response.text, type="html")
    items = selector.xpath("//div[@class='document-update']/ul/li")
    print("搜索关键词条数：{}".format(len(items)))
    for item in items:
        title = item.xpath("string(./div)").get("").strip()
        href = item.xpath(".//a/@href").get("").strip()
        if href:
            href = urljoin("https://kb.uniontech.com/", href)
            if word and word in title:
                print("{title}\n{href}\n".format(title=title, href=href))
            elif not word:
                print("{title}\n{href}\n".format(title=title, href=href))


if __name__ == '__main__':
    # filter_ret(get_resp("专业版"), "黑屏")

    if len(sys.argv) <= 1:
        sys.exit()
    else:
        keyword = sys.argv[1]
        print("keyword: ", keyword)
        if len(sys.argv) <= 2:
            filter_word = ''
        else:
            filter_word = sys.argv[2]
            print("filter_word: ", filter_word)
            filter_ret(get_resp(keyword), filter_word)
