import main
import sys

def start():
    url = sys.argv[1]
    phone = "15925650514"
    ti = main.testInfo(url)
    ti.advanceRun(phone)

start()