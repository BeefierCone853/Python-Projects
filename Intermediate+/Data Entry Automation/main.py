from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time


FORM_URL = "https://forms.gle/8YGR2QcLCF2MGUhp8"
RENTAL_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hr-HR;q=0.8,hr;q=0.7,la;q=0.6"
}

response = requests.get(RENTAL_URL, headers = headers)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

rental_prices = soup.find_all("div", class_ = "list-card-price")
rental_prices = [price.getText().split("+")[0] for price in rental_prices]
rental_prices = [price.split("/")[0] for price in rental_prices]
for price in rental_prices:
    if "C" in price:
        rental_prices.append(price.split("C")[1])


rental_addresses_elements = soup.select(".list-card-info address")
rental_addresses = [address.getText().split(" | ")[-1] for address in rental_addresses_elements]


rental_links_elements = soup.select(".list-card-top a")
rental_links = []
for link in rental_links_elements:
    href = link["href"]
    if "http" not in href:
        rental_links.append(f"https://www.zillow.com{href}")
    else:
        rental_links.append(href)


driver = webdriver.Chrome()
driver.get(FORM_URL)

address_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
price_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
link_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
submit_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
submit_another_xpath = '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'

n = 0

while n < len(rental_prices):
    time.sleep(0.3)

    address = driver.find_element(By.XPATH, address_xpath)
    address.send_keys(rental_addresses[n])

    price = driver.find_element(By.XPATH, price_xpath)
    price.send_keys(rental_prices[n])

    link = driver.find_element(By.XPATH, link_xpath)
    link.send_keys(rental_links[n])

    submit = driver.find_element(By.XPATH, submit_xpath)
    submit.click()

    time.sleep(0.3)

    submit_another = driver.find_element(By.XPATH, submit_another_xpath)
    submit_another.click()

    n += 1

driver.quit()
