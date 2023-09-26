import sys
import time

from driver.cli import cliAdd, cliKeepLoop, cliRunStr
from driver.dxl import Dxl

from lib.uart import *

USE_CLI = True


def millis():
  return int(round(time.time() * 1000))

def delay(time_ms):
  time.sleep(time_ms/1000)

def delayUntil(pre_time, time_ms):
  while 1:
    current_time = millis()
    if current_time - pre_time >= time_ms:
      return current_time