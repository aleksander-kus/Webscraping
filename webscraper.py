#!/bin/python3

import json
import subprocess
from selenium import webdriver

class Webscraper():

    def startDriver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = True
        self.driver = webdriver.Chrome(options=chrome_options)
        
    def __init__(self):
        self.path = '/home/student/bin/'
        self.startDriver()
        self.readConfigFile()

    def __del__(self):
        self.driver.close()


if __name__ == "__main__":
    pass