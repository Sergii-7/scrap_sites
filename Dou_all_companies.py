import csv
import time

from dataclasses import dataclass

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

s = Service("C:/Users/Anton/chrome_driver_for_selenium/chromedriver.exe")
BASE_URL = "https://jobs.dou.ua/companies/"


@dataclass
class Company:
    name: str
    website: str
    url: str


def create_file(data: list):

    with open("dou_all_companies.csv", "w", encoding='utf-8', newline="") as file:
        first_row = ["name", "website", "url"]

        writer = csv.writer(file)
        writer.writerow(first_row)
        writer.writerows(data)


def parce_companies():
    driver = webdriver.Chrome(service=s)
    driver.get(BASE_URL)
    companies_info = []

    companies = driver.find_elements(By.CLASS_NAME, "h2")

    for company in companies:
        detailed_info = company.find_element(By.CLASS_NAME, "cn-a")
        detailed_info.click()

        name = driver.find_element(By.CLASS_NAME, "g-h2").text
        try:
            website = driver.find_element(By.CLASS_NAME, "site > a").get_attribute('href')
        except:
            website = "None"
        url = driver.current_url

        company_data = [name, website, url]

        companies_info.append(company_data)
        driver.execute_script("window.history.go(-1)")
        time.sleep(0.5)
    driver.close()
    create_file(companies_info)


if __name__ == "__main__":
    parce_companies()
