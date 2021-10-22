from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://login.salesforce.com/?locale=it")

driver.find_element(By.CSS_SELECTOR, '#username').send_keys("Alessandro")

driver.find_element(By.CSS_SELECTOR, '.password').send_keys("1234567890")
# driver.find_element(By.CSS_SELECTOR, '.password').clear()

# find element by link name
driver.find_element(By.LINK_TEXT, "Password dimenticata?").click()
driver.find_element(By.NAME, "cancel").click()

driver.find_element(By.XPATH, "//form[@name='login']/div[1]/label")
