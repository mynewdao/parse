import requests
from bs4 import BeautifulSoup

URL = "https://cars.kg/offers/"
HEADERS = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "accept" : "*/*"
}
LINK = "https://cars.kg/"

def get_html(headers, url, params = None):
    response = requests.get(url, params=params,headers=headers)
    return response

def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="catalog-list")
    cars = []
    for i in items:
        cars.append({
            "title":i.find("span", class_="catalog-item-caption").get_text().replace("\n", "").replace("  ", " "),
            "image":i.find("img").get("src"),
            "description": i.find("span", class_="catalog-item-descr").get_text().replace("\n", "").replace(" ", ""),
            "price": i.find("span", class_="catalog-item-price").get_text().replace("\n", "").replace(" ", "")
        })
    print(cars)

def get_parse_result():
    html = get_html(url = URL, headers = HEADERS)
    # print(html.text)
    get_content(html.text)


get_parse_result()


