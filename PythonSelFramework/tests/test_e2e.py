import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.CheckoutPage import CheckoutPage
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures('setup')
class TestOne(BaseClass):
    def test_e2e(self):

        log = self.getLogger()

        # self.driver.find_element_by_xpath("//a[normalize-space()='Shop']").click()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        log.info('getting all the product titles')

        products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        # checkoutPage = CheckoutPage(self.driver)
        for product in products:
            productName = product.text
            print(productName)
            # log.info(productName)
            if productName == 'Blackberry':
                # product.find_element_by_xpath('div[2]/button').click()
                checkoutPage.productNameButton().click()

        # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        # self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        checkoutPage.checkOutItems().click()
        confirmPage = checkoutPage.checkOutItems2()
        log.info('Entering country name as ind')

        self.driver.find_element_by_id('country').send_keys('ind')
        # wait = WebDriverWait(self.driver, 7)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))
        self.verifyLinkPresence('India')


        # self.driver.find_element_by_link_text('India').click()
        # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        # self.driver.find_element_by_xpath("//input[@value='Purchase']").click()
        confirmPage.dropdownMenu().click()
        confirmPage.checkBox().click()
        confirmPage.purchaseButton().click()

        successText = self.driver.find_element_by_class_name("alert-success").text
        log.info('Text received from application is ' + successText)
        assert 'Success! Thank you!' in successText
        self.driver.get_screenshot_as_file('screen.png')