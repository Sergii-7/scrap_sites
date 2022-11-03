import time

from bs4 import BeautifulSoup
from requests.structures import CaseInsensitiveDict
import requests

BASE_URL = "https://jobs.dou.ua/companies/"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0"
}


def dou_pagination():

    url = "https://jobs.dou.ua/companies/xhr-load/?"

    headers = CaseInsensitiveDict()
    headers["authority"] = "jobs.dou.ua"
    headers["accept"] = "application/json, text/javascript, */*; q=0.01"
    headers["accept-language"] = "uk,en;q=0.9"
    headers["content-type"] = "application/x-www-form-urlencoded; charset=UTF-8"
    headers["cookie"] = "_ga=GA1.2.906970660.1659618555; _fbp=fb.1.1659618555009.1311807100; csrftoken=6Sku31NuiqUNI4y7mA4uCVtGmkbzZVwgiOBbg6JwmVz1xe5XAmNSRyKrcodw1r1W; sessionid=7p0pg7l79o6j3xllkt5f7kn833notwuo; __gsas=ID=d65e07633984e033:T=1665147874:S=ALNI_MZuub5ea5WDBwhReN4IicffbPmP9A; _gid=GA1.2.1768335354.1666982786"
    headers["origin"] = "https://jobs.dou.ua"
    headers["referer"] = "https://jobs.dou.ua/companies/"
    headers["sec-ch-ua"] = '"Google Chrome";v="107", "Chromium";v="107", "Not = A?Brand";v="24"'
    headers["sec-ch-ua-mobile"] = "?0"
    headers["sec-ch-ua-platform"] = '"Windows"'
    headers["sec-fetch-dest"] = "empty"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-site"] = "same-origin"
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    headers["x-requested-with"] = "XMLHttpRequest"

    payload = "csrfmiddlewaretoken=cVtAxyfwKbsWnOUV1oxCeW4l1gBAbDFXoRKhKDbyOG7acYrLfag0tzl6RkDxd9aD&count=80"

    resp = requests.post(url, headers=headers, data=payload)
    time.sleep(5)
    print(resp.status_code)

    page = requests.get(BASE_URL, headers=HEADERS).content
    soup = BeautifulSoup(page, "html.parser")
    companies = soup.select(".h2")

    for company in companies:
        name = company.select_one(".cn-a").text
        print(name)


dou_pagination()
