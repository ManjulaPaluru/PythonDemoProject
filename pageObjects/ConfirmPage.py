from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ConfirmPage:
    def __init__(self,driver):
        self.driver = driver

#self.driver.find_element(By.ID, "country").send_keys("ind")
    #wait = WebDriverWait(self.driver, 20)
    #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    #self.driver.find_element(By.LINK_TEXT, "India").click()
    country = (By.ID, "country")
    countryName = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.XPATH, "//input[@type='submit']")

    def getCountry(self):
        return self.driver.find_element(*self.country)

    def select_country(self, text):
        self.driver.find_element(*self.country).send_keys(text)
        return self.wait_for_country_name()

    def wait_for_country_name(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located((self.countryName)))
        return self.driver.find_element(*self.countryName)

    def select_checkbox(self):
        return self.driver.find_element(*self.checkbox)

    def submit_page(self):
        return self.driver.find_element(*self.submit)
