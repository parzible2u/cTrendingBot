from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.proxy import Proxy, ProxyType
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import requests
from selenium.webdriver.chrome.options import Options


HOSTNAME = ''
PORT = ''
DRIVER = 'CHROME'

def smartproxy():
  prox = Proxy()
  prox.proxy_type = ProxyType.MANUAL
  prox.http_proxy = '{hostname}:{port}'.format(hostname = HOSTNAME, port = PORT)
  prox.ssl_proxy = '{hostname}:{port}'.format(hostname = HOSTNAME, port = PORT)
  if DRIVER == 'FIREFOX':
    capabilities = webdriver.DesiredCapabilities.FIREFOX
  elif DRIVER == 'CHROME':
    capabilities = webdriver.DesiredCapabilities.CHROME
  prox.add_to_capabilities(capabilities)
  return capabilities

def main():
    for i in range(4):
        try:
            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), desired_capabilities=smartproxy())
            browser.maximize_window()
            browser.get('https://coinmarketcap.com')
            browser.implicitly_wait(10)
            element = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div/div[2]/div[4]/div/div[1]")
            element.click()
            element = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div/div[2]/div[5]/div/div/div/div/div[1]/div[1]/div[1]/input")
            element.send_keys('Global Smart Asset')
            browser.implicitly_wait(50)
            element = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div/div[2]/div[5]/div/div/div/div/div[2]/div[1]/a[1]/div/div[2]/div[1]/div")
            element.click()
            browser.implicitly_wait(10)
            total_height = int(browser.execute_script("return document.body.scrollHeight"))
            for i in range(1, total_height, 4):
                browser.execute_script("window.scrollTo(0, 1750);".format(i))

            browser.implicitly_wait(1) 
            element = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[6]/div/div[2]/div/button[1]")
            element.click()
            browser.delete_all_cookies()
            browser.quit()
        except Exception as exc:
            pass

main()