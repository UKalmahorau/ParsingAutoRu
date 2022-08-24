import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://auto.ru/")

# находим и нажимаем кнопку "Я согласен"
accept_button = browser.find_element(By.ID, "confirm-button")
accept_button.click()

# Кликаем по разделу “LADA”
lada_button = browser.find_element(By.CSS_SELECTOR, '[href="https://auto.ru/cars/vaz/all/"]')
lada_button.click()
time.sleep(2)

# Кликаем по переключателю “В кредит”
credit_box = browser.find_element(By.CLASS_NAME, 'Checkbox__checkbox')
credit_box.click()
time.sleep(5)

# Кликаем по кнопке “Показать предложения”
offers_button = browser.find_element(By.CLASS_NAME, 'ButtonWithLoader__content')
offers_button.click()
time.sleep(5)

# Выводим на экран цены на автомобили
prices = browser.find_elements(By.CLASS_NAME, 'ListingItemPrice__content')
for price in prices:
    print(price.text)

# Не удалось выполнить бонусное сложное задание:
# Выведите модель самого дешевого автомобиля

browser.close()
