from define import *

from gui.launcher.gui import LauncherGui
from gui.protocol_handler.gui import ProtocolHandlerGui

guis = [
  LauncherGui,
  ProtocolHandlerGui
]


class GuiThread(QThread):
  def __init__(self):
    super().__init__()
    self.is_init = False
    self.name = "Gui"
    self.pre_time = 0
    self.is_loop = False
    self.is_end = False
    self.is_all_gui_shown = False

    self.gui_list = []
    for gui in guis:
      self.gui_list.append(gui())

    for gui in self.gui_list:
      while gui.is_init == False:
        delay(1)
      gui.show()

    self.is_all_gui_shown = True

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
        print("is_all_gui_shown :", self.is_all_gui_shown)
      elif args[0] == "list":
        print("----- Gui List -----")
        for gui in self.gui_list:
          print(gui.name)
        print("--------------------")
      else:
        ret = False

    if len(args) == 2:
      ret = True
      idx = int(args[1])

      if idx >= len(self.gui_list):
        print("index out of range")
      elif args[0] == "geomatry":
        while cliKeepLoop():
          print("pos x  : {0:5d}".format(self.gui_list[idx].x()))
          print("pos y  : {0:5d}".format(self.gui_list[idx].y()))
          print("width  : {0:5d}".format(self.gui_list[idx].width()))
          print("height : {0:5d}".format(self.gui_list[idx].height()))
          print('\x1b[6A')
        print('\x1b[4B')
      elif args[0] == "enable":
        self.gui_list[idx].show()
      elif args[0] == "disable":
        self.gui_list[idx].hide()
      else:
        ret = False

    if ret == False:
      print("gui info")
      print("gui list")
      print("gui geomatry idx0~{0}".format(len(self.gui_list)-1))
      print("gui enable idx0~{0}".format(len(self.gui_list)-1))
      print("gui disable idx0~{0}".format(len(self.gui_list)-1))