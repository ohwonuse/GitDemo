from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    dropdown = (By.LINK_TEXT, 'India')
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.XPATH, "//input[@value='Purchase']")

    def dropdownMenu(self):
        return self.driver.find_element(*ConfirmPage.dropdown)

    def checkBox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def purchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchase)