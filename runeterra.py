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

    def run(self):
        old_titles = [line.rstrip('\n') for line in self.titles_file]
        new_titles = self.get_new_titles_from_source()
        titles = self.compare_old_and_new_titles(old_titles, new_titles)
        if len(titles) == 0:
            return
        msg = self.compose_message(titles)
        send_message.send_message(msg[0], msg[1])
        self.update_titles(new_titles)


    def __del__(self):
        self.source.close()
        self.titles_file.close()
        

if __name__ == "__main__":
    pass