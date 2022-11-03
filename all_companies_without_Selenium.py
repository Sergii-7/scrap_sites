import csv
import requests
from bs4 import BeautifulSoup
import time


BASE_URL = "https://jobs.dou.ua/companies/"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0"
}

results = []


def create_file(data: list):

    with open("dou_all_companies.csv", "w", encoding="utf-8", newline="") as file:
        first_row = ["name", "url", "website", "size", "description"]

        writer = csv.writer(file)
        writer.writerow(first_row)
        for item in data:
            writer.writerow([item["name"], item["url"], item["website"], item["size"], item["description"]])


def get_all_companies():

    page = requests.get(BASE_URL, headers=HEADERS).content
    soup = BeautifulSoup(page, "html.parser")
    companies = soup.select(".h2")
    for company in companies:
        name = company.select_one(".cn-a").text,
        url = company.find("a", {"class": "cn-a"}).get("href")

        detailed_page = requests.get(url, headers=HEADERS).content
        detailed_soup = BeautifulSoup(detailed_page, "html.parser")

        about = detailed_soup.select_one(".b-typo").text.replace("\xa0", " ")
        description = about if len(about) > 10 else "Not available"

        info = detailed_soup.select_one(".company-info")
        size = info.find("h1", class_="g-h2", id=False).find_next_sibling(text=True).text.strip()

        try:
            website = info.a.attrs["href"]
        except AttributeError:
            website = "Not provided"

        results.append(
            {
                "name": name,
                "url": url,
                "website": website,
                "size": size,
                "description": description
            }
        )
    create_file(results)


if __name__ == "__main__":
    print("Starting to parse...")
    start = time.perf_counter()
    get_all_companies()
    end = time.perf_counter()
    print("Done")
    print("Elapsed:", end - start)
