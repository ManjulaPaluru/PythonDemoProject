import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testdata.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class Test_HomePage(BaseClass):
    def test_formsubmission(self,getdata):
        homepage = HomePage(self.driver)
        homepage.get_name().send_keys(getdata["FirstName"])
        homepage.get_email().send_keys(getdata["LastName"])
        homepage.get_password().send_keys("pwd4123")
        homepage.get_checkbox().click()
        self.selectOptionByText(homepage.get_gender(),getdata["Gender"])

        self.driver.find_element(By.XPATH, "//input[@id='inlineRadio1']").click()
        self.driver.find_element(By.XPATH, "//input[@class='form-control' and @name='bday']").click()
        self.driver.find_element(By.XPATH, "(//input[@type='text' and @name='name'])[2]").send_keys("hiiiiii")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()
        message = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        print(message)
        assert "Success" in message
        self.driver.refresh()


   # @pytest.fixture(params=HomePageData.test_HomePage_data)
    @pytest.fixture(params=HomePageData.get_text_data("TestCase1"))
    def getdata(self,request):
        return request.param



