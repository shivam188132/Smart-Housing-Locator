import random
import time

import pandas
from bs4 import BeautifulSoup
from selenium import webdriver


class WebScrapping:
    def __init__(self):
        self.property_link = ''
        self.property_address = ''
        self.price_list = []
        self.prices = ""
        self.data = pandas.read_csv("Free_Proxy_List.csv", on_bad_lines='skip')
        self.ip_list = self.data["ip"].to_list()
        self.proxy = random.choice(self.ip_list)
        self.property_address_list = []
        self.property_link_list = []
        self.url = 'https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.7515891928711%2C%22east%22%3A-122.1150688071289%2C%22south%22%3A37.586721689943616%2C%22north%22%3A37.96338147229348%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
        self.driver = webdriver.Chrome()  # Make sure you have Chrome driver installed and added to PATH
        self.driver.get(self.url)
        time.sleep(10)  # Wait for JavaScript to execute and load the content
        self.web_page = self.driver.page_source
        self.soup = BeautifulSoup(self.web_page, "html.parser")
        self.attribute_name = 'data-test'
        self.price_attribute_name = 'data-test'
        self.master_url = 'https://www.zillow.com'

    def property_address_details(self):
        self.property_address = self.soup.find_all('address', attrs={self.price_attribute_name: 'property-card-addr'})
        for address in self.property_address:
            self.property_address_list.append(address.text)
        return self.property_address_list

    def property_price(self):
        self.prices = self.soup.find_all('span', attrs={self.attribute_name: 'property-card-price'})
        for price in self.prices:
            self.price_list.append(price.text)
        return self.price_list

    def property_scraped_link(self):
        self.property_link = self.soup.find_all('a', attrs={self.attribute_name: 'property-card-link'})
        for item_url in self.property_link:
            # Use the .get('href') method to get the value of the 'href' attribute
            link = item_url.get('href')
            if link and link.startswith('/'):
                link = self.master_url + link
                self.property_link_list.append(link)

        return self.property_link_list



