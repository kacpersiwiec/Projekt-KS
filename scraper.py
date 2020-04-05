#import bibliotek
import requests
from bs4 import BeautifulSoup
import pprint
import json


# nawiązanie połaczenia ze strona i pobranie kodu
url_prefix = "https://www.ceneo.pl"
url_postfix = "/85910996#tab=reviews_scroll"
url = url_prefix + url_postfix
# url = "https://www.ceneo.pl/85910996#tab=reviews_scroll"
response = requests.get(url)
page_dom = BeautifulSoup(response.text, "html.parser")


all_opinions = []

while url:
    # pobieranie kodu pojedynczej opinii
    response = requests.get(url)
    page_dom = BeautifulSoup(response.text, "html.parser")

    # wydobycie z kodu fragmentów odpowiadajacych opiniom konsumentów
    opinions = page_dom.select("li.js_product-review")

    # dla pojedynczej opinii wydobycie jej składowych
    for opinion in opinions:
        opinion_id = opinion["data-entry-id"]
        author = opinion.select("div.reviewer-name-line").pop().text.strip()

        try:
            recommendation = opinion.select(
                "div.product-review-summary > em").pop().text.strip()
        except IndexError:
            recommendation - None

        stars = opinion.select("span.review-score-count").pop().text.strip()
        content = opinion.select("p.product-review-body").pop().text.strip()

        try:
            cons = opinion.select("div.cons-cell > ul").pop().text.strip()
        except IndexError:
            cons = None

        try:
            pros = opinion.select("div.pros-cell > ul ").pop().text.strip()
        except IndexError:
            pros = None

        useful = opinion.select("button.vote-yes > span").pop().text.strip()
        useless = opinion.select("button.vote-no > span").pop().text.strip()
        try:
            opinion_date = opinion.select(
                "span.review-time > time:nth-child(1)").pop()["datetime"].text.strip()
        except IndexError:
            opinion_date = None

        try:
            purchase_date = opinion.select(
                "span.review-time > time:nth-child(2)").pop()["datetime"].text.strip()
        except IndexError:
            purchase_date = None

        features = {
            "opinion_id": opinion_id,
            "author": author,
            "recommendation": recommendation,
            "stars": stars,
            "content": content,
            "cons": cons,
            "pros": pros,
            "useful": useful,
            "useless": useless,
            "opinion_date": opinion_date,
            "purchase_date": purchase_date
        }
        all_opinions.append(features)
    try:
    url = url_prefix+page_dom.select("a.pagination_next").pop()["href"]
    except IndexError:
        url = None
    print(len(all_opinions))
    print(url)
with open('opinions.json', 'w', encoding="UTF-8") as fp:
    json.dump(all_opinions, fp, indent=4, ensure_ascii=False)
    # pprint.pprint(all_opinions)
    #print(opinion_id, author, stars, content, cons, pros,useful, useless, opinion_date, purchase_date)
