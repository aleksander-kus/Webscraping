#!/bin/python3

import json
import subprocess
from os import getcwd
from selenium import webdriver

class Webscraper():

    def startDriver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = True
        self.driver = webdriver.Chrome(options=chrome_options)
        
    def __init__(self):
        self.path = getcwd() + '/'
        self.startDriver()
        self.readConfigFile()

    def readConfigFile(self):
        with open(self.path + '.config/webscraper.json') as f:
            config = json.load(f)
        if 'scripts' in config:
            self.scripts = config['scripts']
        else:
            print("wrong JSON config file format")
            exit(-1)

    def runScripts(self):
        try:
            for script in self.scripts:
                self.processScript(script)
        except:
            print("wrong JSON config file format")
            exit(-1)

    def processScript(self, script):
        if script['enabled'] == False:
            return
        if script['login']['required'] == True:
            getattr(self, script['login']['method'])()
        self.driver.get(script['url'])
        with open(self.path + script['html'], "w") as f:
            f.write(self.driver.page_source)
        subprocess.Popen(['python3', self.path + script['source']])

    def __del__(self):
        self.driver.close()


if __name__ == "__main__":
    scraper = Webscraper()
    scraper.runScripts()