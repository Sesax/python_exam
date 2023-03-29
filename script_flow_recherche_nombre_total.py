
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome()
driver.get("https://demo.kestra.io/ui/login?from=/ui/")
driver.set_window_size(1623, 1040)
time.sleep(1)
driver.find_element(
    By.CSS_SELECTOR, ".el-button--info > span").click()
time.sleep(1)
driver.find_element(
    By.XPATH, '//*[@id="side-menu"]/div[2]/div/div[1]/ul/li[2]/a/div/span').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.el-input__inner').click()
time.sleep(1)
driver.find_element(
    By.CSS_SELECTOR, '.el-input__inner').send_keys("a")
time.sleep(1)

WebDriverWait(driver, 10).until(
    expected_conditions.visibility_of_element_located(
        (By.CSS_SELECTOR, ".el-table__row"))
)

rows = driver.find_elements(By.CSS_SELECTOR, ".el-table__row")
time.sleep(1)
total = driver.find_element(
    By.XPATH, '//*[@id="app"]/main/div/div/div/section/div[3]/small').text
time.sleep(1)

nb_result = len(rows)

print("Affichés: ", nb_result)
print(total)
