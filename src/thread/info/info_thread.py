from define import *

class InfoThread(QThread):
  def __init__(self):
    super().__init__()
    self.is_init = False
    self.name = "Info"
    self.pre_time = 0
    self.is_loop = False
    self.is_end = False

    cliAdd("info", self.cliCmd)

    self.is_init = True

  def __del__(self):
    self.is_loop = False
    while self.is_end == False:
      delay(1)

  def run(self):
    self.pre_time = millis()

    self.is_loop = True
    while self.is_loop:
      
      if USE_CLI == True:
        cliMain()

      self.pre_time = delayUntil(self.pre_time, 5)
    self.is_end = True

  def cliCmd(self, args):
    ret = False

    if ret == False:
      pass
      #print("info")