from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# browser exposes an executable file, I invoke them from selenium
# driver = webdriver.Chrome(executable_path="C:\\Users\\gul4s\\Downloads\\Python\\PythonBasics\\chromedriver.exe")
driver = Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Find element by Name
# driver.find_element(By.NAME, "name").send_keys("Pino")

# Find element by Id
# driver.find_element(By.ID, "exampleCheck1").click()

# Often there are several element with the same tags or name, you can check in the browser console
# $( tag [ attribute = "value" ] ) example => $(input[name='name'])
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("alessandro")
driver.find_element(By.NAME, "email").send_keys("alessandro@mail.it")

driver.find_element(By.ID, "exampleCheck1").click()

# select class provide the methods to handle the options in dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
# dropdown.deselect_by_visible_text("Female")
# dropdown.select_by_index(0)

# To search element using xpath in the browser console you can use
# $x("//input[@type='submit']")
# you can also use ChroPath extension to find the xPath automatically
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# Success! The Form has been submitted successfully!.
message = driver.find_element(By.CLASS_NAME, "alert-success").text

# assert aspect true in the condition
assert "Success" in message
