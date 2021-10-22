import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

for country in countries:
    if country.text == "India":
        country.click()
        break

# use get_attribute value to get the test into the search bar
countrySelected = driver.find_element(By.ID, "autosuggest").get_attribute('value')
assert countrySelected == "India"
