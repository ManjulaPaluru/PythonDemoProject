from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self,driver):
        self.driver = driver

#phonename.find_element(By.XPATH, "[3]").click()
# checkoutItems = self.driver.find_element(By.XPATH, "//a[contains(text(),'Checkout')]")
    # self.driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()
    #self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
    phoneList = (By.XPATH, "//a/parent::h4")
    phoneName = (By.XPATH,"[3]")
    checkoutItems = (By.XPATH, "//a[contains(text(),'Checkout')]")
    checkoutButton = (By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
    checkOutSuccess = (By.CSS_SELECTOR, ".btn.btn-success")

    def getPhoneList(self):
         return self.driver.find_elements(*CheckOutPage.phoneList)
    def getphoneName(self):
        return self.driver.find_element(*CheckOutPage.phoneName)

    def getCheckOutItems(self):
        return self.driver.find_element(*CheckOutPage.checkoutItems)

    def clickCheckoutButton(self):
         return self.driver.find_element(*CheckOutPage.checkoutButton)

    # self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
    def checkOutButtonSuccess(self):
         self.driver.find_element(*CheckOutPage.checkOutSuccess).click()
         confirm_page = ConfirmPage(self.driver)
         return confirm_page