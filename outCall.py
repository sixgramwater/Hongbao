import newSim
import newTest
import sys


def start(url, phone="15925650514"):
    ti = newTest.testInfo(url)
    msg = ti.advanceRun(phone)
    return msg
