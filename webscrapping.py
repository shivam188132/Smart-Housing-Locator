import requests
from bs4 import BeautifulSoup


class WebScrapping:
    def __init__(self):
        self.property_address_list = ""
        self.response = requests.get(
            url='https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.7515891928711%2C%22east%22%3A-122.1150688071289%2C%22south%22%3A37.586721689943616%2C%22north%22%3A37.96338147229348%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D')
        self.web_page = self.response.text
        self.soup = BeautifulSoup(self.web_page, "html.parser")


    def property_details(self):

        self.property_address_list = self.soup.find_all('address', {'data-test': 'property-card-addr'})
        for address in self.property_address_list:
            print(address.text)














scrapping = WebScrapping()
scrapping.property_details()