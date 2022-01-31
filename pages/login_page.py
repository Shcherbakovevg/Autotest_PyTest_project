from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    
    def register_new_user(self,email, password):
        Email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        Email_input.send_keys(email)
        Password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        Password_input.send_keys(password)    
        Password_repeat = self.browser.find_element(*LoginPageLocators.PASSWORD_REPEAT)
        Password_repeat.send_keys(password)
        Button_submit = self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTRATION_BUTTON)
        Button_submit.click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form not found"
   
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Substring 'login' in link not found"
