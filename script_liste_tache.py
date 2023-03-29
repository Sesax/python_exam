
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# DEFINIR LE NAMESPACE ET L'IDENTIFIANT ICI

namespace = "io.kestra.demo.google"
identifiant = "python-script-with-pip-package-bigquery-load"


driver = webdriver.Chrome()
driver.get("https://demo.kestra.io/ui/login?from=/ui/")
driver.set_window_size(1623, 1040)
time.sleep(1)
driver.find_element(
    By.CSS_SELECTOR, ".el-button--info > span").click()
time.sleep(1)

driver.get("https://demo.kestra.io/ui/flows/edit/" +
           namespace+"/"+identifiant+"/topology")

time.sleep(1)
rows = driver.find_elements(
    By.CSS_SELECTOR, ".task-title")
time.sleep(1)

for row in rows:
    print(row.text)
