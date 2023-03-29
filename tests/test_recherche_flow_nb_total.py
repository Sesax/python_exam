import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestFlowrecherchenombretotal():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_flowrecherchenombretotalV1(self):

        # LE TEST DOIT RENVOYER 25 LIGNES ET 26 RESULTATS AU TOTAL

        self.driver.get("https://demo.kestra.io/ui/login?from=/ui/")
        self.driver.set_window_size(1623, 1040)
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, ".el-button--info > span").click()
        time.sleep(1)
        self.driver.find_element(
            By.XPATH, '//*[@id="side-menu"]/div[2]/div/div[1]/ul/li[2]/a/div/span').click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '.el-input__inner').click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, '.el-input__inner').send_keys("a")
        time.sleep(1)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, ".el-table__row"))
        )

        rows = self.driver.find_elements(By.CSS_SELECTOR, ".el-table__row")
        time.sleep(1)
        total = self.driver.find_element(
            By.XPATH, '//*[@id="app"]/main/div/div/div/section/div[3]/small').text
        time.sleep(1)

        nb_result = len(rows)

        # TEST DES RESULTATS

        assert (nb_result == 25)
        assert (total == "Total: 26")

    def test_flowrecherchenombretotalV2(self):

        # LE TEST DOIT RENVOYER 2 LIGNES ET 2 RESULTATS AU TOTAL

        self.driver.get("https://demo.kestra.io/ui/login?from=/ui/")
        self.driver.set_window_size(1623, 1040)
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, ".el-button--info > span").click()
        time.sleep(1)
        self.driver.find_element(
            By.XPATH, '//*[@id="side-menu"]/div[2]/div/div[1]/ul/li[2]/a/div/span').click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '.el-input__inner').click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, '.el-input__inner').send_keys("python")
        time.sleep(1)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, ".el-table__row"))
        )

        rows = self.driver.find_elements(By.CSS_SELECTOR, ".el-table__row")
        time.sleep(1)
        total = self.driver.find_element(
            By.XPATH, '//*[@id="app"]/main/div/div/div/section/div[3]/small').text
        time.sleep(1)

        nb_result = len(rows)

        # TEST DES RESULTATS

        assert (nb_result == 2)
        assert (total == "Total: 2")
