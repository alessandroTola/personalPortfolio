from selenium import webdriver
#browser exposes an axecutable file, I invoke them from selenium
driver = webdriver.Chrome(executable_path="C:\\Users\\gul4s\\Downloads\\Python\\PythonBasics\\chromedriver.exe")

driver.get("http://www.google.com")