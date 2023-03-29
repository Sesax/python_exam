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


class TestListeTache():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_listetacheV1(self):

        # LE TEST DOIT RENVOYER ["schedule", "download", "load"]

        namespace = "io.kestra.demo.google"
        identifiant = "python-script-with-pip-package-bigquery-load"

        self.driver.get("https://demo.kestra.io/ui/login?from=/ui/")
        self.driver.set_window_size(1623, 1040)
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, ".el-button--info > span").click()
        time.sleep(1)

        self.driver.get("https://demo.kestra.io/ui/flows/edit/" +
                        namespace+"/"+identifiant+"/topology")

        time.sleep(1)
        rows = self.driver.find_elements(
            By.CSS_SELECTOR, ".task-title")
        time.sleep(1)

        # TEST DES RESULTATS

        assert (rows[0].text == "schedule")
        assert (rows[1].text == "download")
        assert (rows[2].text == "load")

    def test_listetacheV2(self):

        # LE TEST DOIT RENVOYER ["allow-failure", "seq", "log1", "ko", "log2", "last"]

        namespace = "io.kestra.demo.flows"
        identifiant = "allow-failure"

        self.driver.get("https://demo.kestra.io/ui/login?from=/ui/")
        self.driver.set_window_size(1623, 1040)
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, ".el-button--info > span").click()
        time.sleep(1)

        self.driver.get("https://demo.kestra.io/ui/flows/edit/" +
                        namespace+"/"+identifiant+"/topology")

        time.sleep(1)
        rows = self.driver.find_elements(
            By.CSS_SELECTOR, ".task-title")
        time.sleep(1)

        # TEST DES RESULTATS

        assert (rows[0].text == "allow-failure")
        assert (rows[1].text == "seq")
        assert (rows[2].text == "log1")
        assert (rows[3].text == "ko")
        assert (rows[4].text == "log2")
        assert (rows[5].text == "last")

    def test_listetacheV3(self):

        # LE TEST DOIT RENVOYER ["pause", "wait-manual", "last"]

        namespace = "io.kestra.demo.flows"
        identifiant = "pause"

        self.driver.get("https://demo.kestra.io/ui/login?from=/ui/")
        self.driver.set_window_size(1623, 1040)
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, ".el-button--info > span").click()
        time.sleep(1)

        self.driver.get("https://demo.kestra.io/ui/flows/edit/" +
                        namespace+"/"+identifiant+"/topology")

        time.sleep(1)
        rows = self.driver.find_elements(
            By.CSS_SELECTOR, ".task-title")
        time.sleep(1)

        # TEST DES RESULTATS

        assert (rows[0].text == "pause")
        assert (rows[1].text == "wait-manual")
        assert (rows[2].text == "last")
