from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
from datetime import datetime

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_driver_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe"
chrome_service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)
driver.maximize_window()


driver.get('http://localhost:3000/')

def waitForAndGetElem(elementId):

    try:
        element_present = EC.presence_of_element_located((By.ID, elementId))
        WebDriverWait(driver, 30).until(element_present)

        element_clickable = EC.element_to_be_clickable((By.ID, elementId))
        WebDriverWait(driver, 30).until(element_clickable)

        element = driver.find_element(By.ID, elementId)

        return element
    except:
        raise

with open('data.csv', 'r') as file:
     csv_reader = csv.DictReader(file)

     for row in csv_reader:

        searchBar = waitForAndGetElem('MID')
        searchBar.send_keys(row['MID'])
        time.sleep(1)
        searchBtn = waitForAndGetElem('searchBtn')
        searchBtn.click()

        commentBar = waitForAndGetElem('commentField')
        commentBar.send_keys(row['Comment'])
        time.sleep(1)
        commentBtn = waitForAndGetElem('commentBtn')
        commentBtn.click()
        time.sleep(2)
        print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Comment Added:', row['MID'], row['Comment'])

file.close()
driver.close()
