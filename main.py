import time
from brain import WebScrapping

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

scrapping = WebScrapping()
address = scrapping.property_address_details()
price = scrapping.property_price()
link = scrapping.property_scraped_link()




google_form_link = "https://docs.google.com/forms/d/e/1FAIpQLSdLLoiswihQx9ncTZPft_WkGr-6vi_7wa8ENfjQnb4OYX2PBA/viewform?usp=sf_link"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url=google_form_link)
time.sleep(5)

def Sheets():

        for addr, prc, lnk in zip(address, price, link):
            question_1 = driver.find_element(By.XPATH,
                                             '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            question_1.send_keys(addr)
            time.sleep(1)

            question_2 = driver.find_element(By.XPATH,
                                             '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            question_2.send_keys(prc)
            time.sleep(1)

            question_3 = driver.find_element(By.XPATH,
                                             '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            question_3.send_keys(lnk)
            time.sleep(1)

            submit_btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
            submit_btn.click()

            time.sleep(2)
            another_response = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
            another_response.click()
            time.sleep(3)

        print("done")

Sheets()