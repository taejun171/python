from define import *
from PySide6.QtCore import QThread


from driver.gui import MainWindow


class GuiThread(QThread):
  def __init__(self):
    super().__init__()
    self.is_init = False
    self.name = "Gui"
    self.pre_time = 0
    self.is_loop = False
    self.is_end = False

    self.window = MainWindow()
    self.window.show()

    cliAdd("gui", self.cliCmd)

    self.is_init = True

  def __del__(self):
    self.is_loop = False
    while self.is_end == False:
      delay(1)

  def run(self):
    self.pre_time = millis()

    self.is_loop = True
    while self.is_loop:
      
      

      self.pre_time = delayUntil(self.pre_time, 5)
    self.is_end = True

  def cliCmd(self, args):
    ret = False

    if len(args) == 1:
      ret = True

      if args[0] == "info":
        while cliKeepLoop():
          print("pos x  :", self.window.x())
          print("pos y  :", self.window.y())
          print("width  :", self.window.width())
          print("height :", self.window.height())
          print('\x1b[6A')
        print('\x1b[4B')
      elif args[0] == "enable":
        self.window.show()
      elif args[0] == "disable":
        self.window.hide()
      elif args[0] == "close":
        self.window.deleteLater()
      else:
        ret = False

    if ret == False:
      print("gui info")
      print("gui enable")
      print("gui disable")
      print("gui close")