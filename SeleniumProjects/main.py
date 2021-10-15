from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
#browser exposes an axecutable file, I invoke them from selenium
#driver = webdriver.Chrome(executable_path="C:\\Users\\gul4s\\Downloads\\Python\\PythonBasics\\chromedriver.exe")
driver = Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "name").send_keys("Pino")
driver.find_element(By.ID, "exampleCheck1").click()
