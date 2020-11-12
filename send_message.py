import subprocess

def send_message(title, content):
    subprocess.Popen(['notify-send', title, content])