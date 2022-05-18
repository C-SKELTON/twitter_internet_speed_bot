from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv


load_dotenv("C:/Users/conno/PycharmProjects/.env.txt")


chrome_driver_path = Service("C:/Users/conno/chrome_driver/chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=chrome_driver_path, options=op)
promised_down = 400
promised_up = 200
twitter_username = os.getenv("tw_user")
twitter_password = os.getenv("tw_pass")


class InternetSpeedTwitterBot:

    def __init__(self, driver):
        self.website = driver
        self.download = promised_down
        self.upload = promised_up

    def get_internet_speed(self):
        driver.get(self.website)
        time.sleep(5)
        start_btn = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start_btn.click()
        time.sleep(60)
        self.down = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text


    def tweet_at_provider(self):
        driver.get(self.website)
        time.sleep(10)
        login_btn = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        login_btn.click()
        time.sleep(2)
        user_input = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        user_input.send_keys(twitter_username)
        nxt_btn = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        nxt_btn.click()
        time.sleep(2)
        pass_input = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pass_input.send_keys(twitter_password)
        log_in2 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div')
        log_in2.click()
        time.sleep(2)
        self.txt_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        self.txt_field.send_keys('a')
        time.sleep(2)
        self.tweet_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        self.txt_field.send_keys(Keys.BACK_SPACE)


x = InternetSpeedTwitterBot("https://www.speedtest.net/")
x.get_internet_speed()
if float(x.down) < x.download or float(x.up) < x.upload:
    y = InternetSpeedTwitterBot("https://twitter.com/")
    y.tweet_at_provider()
    y.txt_field.clear()
    time.sleep(5)
    y.txt_field.send_keys(str(f"Hey Internet Provider, why is my internet speed {x.down}down/{x.up}up when I pay for {y.download}down/{y.upload}up ?"))
    time.sleep(20)
    y.tweet_btn.click()

driver.quit()