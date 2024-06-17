from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.XPATH, "//select[@id='exampleFormControlSelect1']")


    def shopItems(self):
         self.driver.find_element(*HomePage.shop).click()
         check_out_page = CheckOutPage(self.driver)
         return check_out_page
    def get_name(self):
        return self.driver.find_element(*HomePage.name)
    def get_email(self):
        return self.driver.find_element(*HomePage.email)
    def get_password(self):
        return self.driver.find_element(*HomePage.password)
    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)
    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

