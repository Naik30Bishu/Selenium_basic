from selenium import webdriver
driver=webdriver.Firefox(executable_path="D:\geckodriver.exe")
driver.get("https://www.naukri.com/")
driver.close()

