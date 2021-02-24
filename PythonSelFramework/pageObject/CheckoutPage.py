from selenium.webdriver.common.by import By
from pageObject.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    productNameButton = (By.XPATH, "div[2]/button")
    checkOut = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOut2 = (By.XPATH, "//button[@class='btn btn-success']")

    def getproducts(self):
        return self.driver.find_element(*CheckoutPage.products)

    def productNamebutton(self):
        return self.driver.find_element(*CheckoutPage.productNameButton)

    def checkOutItems(self):
        return self.driver.find_element(*CheckoutPage.checkOut)

    def checkOutItems2(self):
        self.driver.find_element(*CheckoutPage.checkOut2).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage