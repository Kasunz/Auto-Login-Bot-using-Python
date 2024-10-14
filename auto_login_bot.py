from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

class AutoLoginBot:
    def __init__(self, driver_path, website_url, user_name, password):
        """ Initialize the bot with necessary variables """
        self.driver_path = driver_path
        self.website_url = website_url
        self.user_name = user_name
        self.password = password
        self.driver = None

    def start_browser(self):
        """ Start the Chrome browser and navigate to the login page """
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(self.website_url)
        time.sleep(2)

    def login(self):
        """ Fill in the username, password, and log in """
        try:
            # Use the correct field names from the HTML
            email_input = self.driver.find_element(By.NAME, "email")
            password_input = self.driver.find_element(By.NAME, "password")

            email_input.send_keys(self.user_name)
            password_input.send_keys(self.password)

            # Find the login button and click it
            login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()

            time.sleep(5)
            print("Login successful")
        except Exception as e:
            print(f"Error: {e}")

    def close_browser(self):
        """ Close the browser after login """
        self.driver.quit()

def main():
    driver_path = r"D:\...Python Projects\chromedriver-win64\chromedriver.exe"
    website_url = "http://localhost/healthcare_clinic/Login.php"
    user_name = "admin@lk"
    password = "admin"

    # Initialize the auto login bot with credentials
    bot = AutoLoginBot(driver_path, website_url, user_name, password)

    # Start the browser and login
    bot.start_browser()
    bot.login()

    # close the browser  after login
    # bot.close_browser()

if __name__ == '__main__':
    main()
