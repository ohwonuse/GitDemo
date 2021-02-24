from selenium.webdriver.common.by import By
from pageObject.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[normalize-space()='Shop']")
    name = (By.NAME, "name")
    email = (By.NAME, 'email')
    checkbox = (By.ID, 'exampleCheck1')
    gender = (By.ID, 'exampleFormControlSelect1')
    submit = (By.XPATH, '//input[@type="submit"]')
    successMessage = (By.CLASS_NAME, 'alert-success')

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitButton(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMSG(self):
        return self.driver.find_element(*HomePage.successMessage)