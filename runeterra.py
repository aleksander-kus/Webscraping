from bs4 import BeautifulSoup
import difflib
import send_message
import os

class Runeterra():

    def open_files(self):
        self.source = open(self.path + ".config/runeterra_source.html", "r")
        tp_path = self.path + ".config/titles.txt"
        if not os.path.exists(tp_path):
            tmp = open(tp_path, "w")
            tmp.close()
        self.titles_file = open(self.path + ".config/titles.txt", "r")

    def __init__(self):
        self.path = os.getcwd() + '/'
        self.open_files()

    def __del__(self):
        self.source.close()
        self.titles_file.close()
        

if __name__ == "__main__":
    pass