import time
import math
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators

class BasePage():
    
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def click_element(self, how, what):
        try:
            element = self.browser.find_element(how, what)
            element.click()
        except (NoSuchElementException):
            return False
        return True 
   
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_basket_page(self):
        login_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        login_link.click()

    def is_disappeared(self, how, what, timeout=4):
            try:
                WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                    until_not(EC.presence_of_element_located((how, what)))
            except TimeoutException:
                return False
            return True
        
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def open(self):
        self.browser.get(self.url)

    def should_be_login_link(self):
        try:
            self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        except (NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 5).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        time.sleep(1)
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        return True
