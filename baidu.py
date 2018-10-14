
from selenium import webdriver
import time
# driver=webdriver.Firefox()
#"C:\\Program Files\\Mozilla Firefox\\geckodriver.exe"
driver=webdriver.Chrome("C:\\Users\\28100\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
#driver=webdriver.Ie()


driver.get("http://www.baidu.com")
time.sleep(3)

driver.find_element_by_id("kw").send_keys("Selenium2")
time.sleep(3)

driver.find_element_by_id("su").click()
time.sleep(3)

driver.quit()
