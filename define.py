"""
Import
"""
import sys
import time

from lib.cli import cliAdd, cliKeepLoop, cliRunStr, cliMain

from PySide6.QtCore import QThread

from driver.dxl import Dxl
from driver.uart import Uart


"""
Define
"""
USE_CLI = True


"""
Variable
"""
uart = Uart()



"""
Function
"""
def millis():
  return int(round(time.time() * 1000))

def delay(time_ms):
  time.sleep(time_ms/1000)

def delayUntil(pre_time, time_ms):
  while 1:
    current_time = millis()
    if current_time - pre_time >= time_ms:
      return current_time