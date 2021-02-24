from selenium import webdriver

# driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
# driver.maximize_window()
# driver.get('https://rahulshettyacademy.com/#/index')
# print(driver.title)
# print(driver.current_url)
# driver.get('https://rahulshettyacademy.com/AutomationPractice/')
# driver.minimize_window()
# driver.back()
# driver.refresh()
# driver.close()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
# driver.get('https://rahulshettyacademy.com/angularpractice/')
# driver.find_element_by_name('name').send_keys('Rahul')
# driver.find_element_by_id('exampleCheck1').click()
# driver.find_element_by_css_selector('Input[name = "name"]').send_keys('Rahul')
# driver.find_element_by_name('email').send_keys('Shetty')
# driver.find_element_by_xpath('//input[@type="submit"]').click()
# print(driver.find_element_by_class_name('alert-success'). text)
# dropdown = Select(driver.find_element_by_id('exampleFormControlSelect1'))
# dropdown.select_by_visible_text('Female')
# dropdown.select_by_visible_text(0)
# dropdown.select_by_value('')
# message = driver.find_element_by_class_name('alert-success').text
# assert 'success' in message


# driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
# driver.get('https://login.salesforce.com/')
# driver.find_element_by_css_selector('#username').send_keys('Rahul')
# driver.find_element_by_css_selector('.password').send_keys('shetty')
# driver.find_element_by_css_selector('.password').clear()
# driver.find_element_by_link_text('Forgot Your Password?').click()
# driver.find_element_by_xpath('//a[text() = "Cancel"]').click()
# print(driver.find_element_by_xpath('//form[@name="login"]/div[1]/label').text)
# print(driver.find_element_by_css_selector('form[name="login"] label:nth-child(3)').text)


from selenium import webdriver
import time

# driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
# driver.get('https://rahulshettyacademy.com/dropdownsPractise/')
# driver.find_element_by_id('autosuggest').send_keys('ind')
# time.sleep(2)
# countries = driver.find_elements_by_css_selector('li[class="ui-menu-item"] a')
# print(len(countries))
# for country in countries:
#     if country.text == 'India':
#         country.click()
#         break
# assert driver.find_element_by_id('autosuggest').get_attribute('value') == 'India'

# from selenium import webdriver

# driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
# driver.get('https://rahulshettyacademy.com/AutomationPractice/')
# checkboxes = driver.find_elements_by_xpath('//input[@type="checkbox"]')
# print(len(checkboxes))
# for checkbox in checkboxes:
#     if checkbox.get_attribute('value') == 'option2':
#         checkbox.click()
#         assert checkbox.is_selected()
# radiobuttons = driver.find_elements_by_name('radioButton')
# radiobuttons[2].click()
# assert radiobuttons[2].is_selected()
# validateText = 'Option3'
# driver.find_element_by_css_selector('#name').send_keys(validateText)
# driver.find_element_by_id('alertbtn').click()
# alert = driver.switch_to.alert
# print(alert.text)
# alertText = alert.text
# assert validateText in alertText
# alert.accept()
# driver.find_element_by_xpath('//input[@id="confirmbtn"]').click()
# alert = driver.switch_to.alert
# alertText = alert.text
# print(alertText)
# alert.dismiss()


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# list = []
# list2 = []
# driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
# driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
# # driver.implicitly_wait(5)
# driver.find_element_by_xpath('//input[@placeholder="Search for Vegetables and Fruits"]').send_keys('ber')
# time.sleep(4)
# count = len(driver.find_elements_by_xpath('//div[@class="product"]'))
# assert count == 3
# buttons = driver.find_elements_by_xpath('//div[@class="product-action"]/button')
# for button in buttons:
#     list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
#     button.click()
# print(list)
# for i in list:
#     assert 'ber' in i
# driver.find_element_by_xpath('//img[@alt="Cart"]').click()
# driver.find_element_by_xpath('//button[normalize-space()="PROCEED TO CHECKOUT"]').click()
# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'promoCode')))
# veggies = driver.find_elements_by_class_name('product-name')
# for veg in veggies:
#     list2.append(veg.text)
# print(list2)
# assert list == list2
# originalAmount = driver.find_element_by_class_name('discountAmt').text
# driver.find_element_by_class_name('promoCode').send_keys('rahulshettyacademy')
# driver.find_element_by_class_name('promoBtn').click()
# wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))
# print(driver.find_element_by_xpath("//span[@class='promoInfo']").text)
# discountAmount = driver.find_element_by_class_name('discountAmt').text
# assert float(discountAmount) < int(originalAmount)
# amounts = driver.find_elements_by_xpath('//tr/td[5]/p')
# sum = 0
# for amount in amounts:
#     sum = sum + int(amount.text)
# totalAmount = int(driver.find_element_by_class_name('totAmt').text)
# assert sum == totalAmount


# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
# driver.get('https://the-internet.herokuapp.com/windows')
# driver.find_element_by_link_text('Click Here').click()
# childwindow = driver.window_handles[1]
# driver.switch_to.window(childwindow)
# print(driver.find_element_by_tag_name('h3').text)
# driver.close()
# driver.switch_to.window(driver.window_handles[0])
# assert 'Opening a new window' == driver.find_element_by_tag_name('h3').text


# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
# driver.get('https://the-internet.herokuapp.com/iframe')
# driver.switch_to.frame('mce_0_ifr')
# driver.find_element_by_css_selector('#tinymce').clear()
# driver.find_element_by_css_selector('#tinymce').send_keys('I am able to automate')
# driver.switch_to.default_content()
# print(driver.find_element_by_tag_name('h3').text)


from selenium import webdriver
from selenium.webdriver import ActionChains

# driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
# driver.get('https://rahulshettyacademy.com/AutomationPractice/')
# action = ActionChains(driver)
# menu = driver.find_element_by_id('mousehover')
# action.move_to_element(menu).perform()
# childmenu = driver.find_element_by_link_text('Reload')
# action.move_to_element(childmenu).click().perform()


from selenium import webdriver
from selenium.webdriver import ActionChains

# driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
# driver.get('https://chercher.tech/practice/practice-pop-ups-selenium-webdriver')
# driver.implicitly_wait(5)
# action = ActionChains(driver)
# action.context_click(driver.find_element_by_id('double-click')).perform()
# action.double_click(driver.find_element_by_id('double-click')).perform()
# alert = driver.switch_to.alert
# assert 'You double clicked me!!!, You got to be kidding me' == alert.text
# alert.accept()


from selenium import webdriver

# driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
# driver.get('https://rahulshettyacademy.com/AutomationPractice/')
# assert driver.find_element_by_name('show-hide').is_displayed()
# driver.find_element_by_id('hide-textbox').click()
# assert not driver.find_element_by_name('show-hide').is_displayed()


from selenium import webdriver

# driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
# driver.get('https://rahulshettyacademy.com/angularpractice/')
# driver.find_element_by_name('name').send_keys('hello')
# print(driver.find_element_by_name('name').get_attribute('value'))
# print(driver.execute_script("return document.getElementsByName('name')[0].value"))
# shopButton = driver.find_element_by_xpath("//a[normalize-space()='Shop']")
# driver.execute_script("arguments[0].click();", shopButton)
# driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')


from selenium import webdriver

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--start-maximized')
# chrome_options.add_argument('headless')
# chrome_options.add_argument('--ignore-certificate-errors')
# driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options= chrome_options)
# driver.get('https://rahulshettyacademy.com/angularpractice/')
# print(driver.title)


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.find_element_by_xpath("//a[normalize-space()='Shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == 'Blackberry':
        product.find_element_by_xpath('div[2]/button').click()
driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id('country').send_keys('ind')
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))
driver.find_element_by_link_text('India').click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_xpath("//input[@value='Purchase']").click()
successText = driver.find_element_by_class_name("alert-success").text
assert 'Success! Thank you!' in successText
driver.get_screenshot_as_file('screen.png')

