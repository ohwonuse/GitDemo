from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utilities.BaseClass import BaseClass
from pageObject.HomePage import HomePage
from TestData.HomePageData import HomePageData
import pytest

class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        # driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
        # driver.get('https://rahulshettyacademy.com/angularpractice/')

        log = self.getLogger()
        homepage = HomePage(self.driver)

        # driver.find_element_by_name('name').send_keys('Rahul')
        # driver.find_element_by_id('exampleCheck1').click()
        # driver.find_element_by_css_selector('Input[name = "name"]').send_keys('Rahul')
        # driver.find_element_by_name('email').send_keys('Shetty')
        # driver.find_element_by_xpath('//input[@type="submit"]').click()

        log.info('first name is ' + getData['firstname'])
        homepage.getName().send_keys(getData['firstname'])
        homepage.getEmail().send_keys(getData['lastname'])
        homepage.getCheckBox().click()
        # sel = Select(homepage.getGender())
        # sel.select_by_visible_text('Male')
        self.selectOptionByText(homepage.getGender(), getData['gender'])

        homepage.submitButton().click()
        alertText = homepage.getSuccessMSG().text
        assert ('success' in alertText)
        self.driver.refresh()


        # print(driver.find_element_by_class_name('alert-success').text)
        # dropdown = Select(driver.find_element_by_id('exampleFormControlSelect1'))
        # dropdown.select_by_visible_text('Female')
        # dropdown.select_by_visible_text(0)
        # dropdown.select_by_value('')
        # message = driver.find_element_by_class_name('alert-success').text
        # assert 'success' in message

    @pytest.fixture(params=HomePageData.getTestData('Testcase2'))
    def getData(self, request):
        return request.param
