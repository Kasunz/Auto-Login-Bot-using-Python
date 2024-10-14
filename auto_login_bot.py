from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class AutoLoginBot:
    def __init__(self, driver_path, website_url, user_name, password):
        self.driver_path = driver_path
        self.website_url = website_url
        self.user_name = user_name
        self.password = password
        self.driver = None
