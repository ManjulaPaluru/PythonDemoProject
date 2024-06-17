import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_end2end(self):
        log = self.getlogger()
        phonename = []
        #self.driver.find_element(By.LINK_TEXT, "Shop").click()
        homePage = HomePage(self.driver)
        check_out_page = homePage.shopItems()
        log.info("getting all the items")

        #phoneList = self.driver.find_elements(By.XPATH, "//a/parent::h4")

        phoneList = check_out_page.getPhoneList()

        for phone in phoneList:
            phonename.append(phone.text)
            log.info(phonename)
        if phonename == "Nokia Edge":
            #phonename.find_element(By.XPATH, "[3]").click()
            check_out_page.getphoneName().click()

        self.driver.find_element(By.XPATH, "(//button[@class='btn btn-info'])[3]").click()
        self.driver.find_element(By.XPATH, "(//button[@class='btn btn-info'])[4]").click()
        self.driver.find_element(By.XPATH, "(//button[@class='btn btn-info'])[1]").click()
        #checkoutItems = self.driver.find_element(By.XPATH, "//a[contains(text(),'Checkout')]")
        checkoutitems = check_out_page.getCheckOutItems()

        # print(checkoutItems) -->printing web elements
        log.info(checkoutitems.text)
        #self.driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()
        check_out_page.clickCheckoutButton().click()

       # self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
        confirmpage = check_out_page.checkOutButtonSuccess()


        #self.driver.find_element(By.ID, "country").send_keys("ind")
        confirmpage.select_country("ind").click()
       # wait = WebDriverWait(self.driver, 20)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        #self.driver.find_element(By.LINK_TEXT, "India").click()
        # confirmpage.wait_for_country_name().click()

        #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        confirmpage.select_checkbox().click()

        #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        confirmpage.submit_page().click()
        successMessage = self.driver.find_element(By.CLASS_NAME, "alert-dismissible").text
        log.info(successMessage)
        expectedMessage = "Success! Thank you! Your order will be delivered in next few weeks :-)."
        log.info(expectedMessage)
        assert expectedMessage in successMessage
        #assert "Success! Thank you!" in successMessage
        log.info("text received from application is: " +expectedMessage)
        log.info("success")
