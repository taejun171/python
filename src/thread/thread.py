from define import *

from thread.info.info_thread import InfoThread
from thread.gui.gui_thread import GuiThread

threads = [
  InfoThread,
  GuiThread
]


class Thread:
  def __init__(self):
    self.thread_list = []
    self.is_all_thread_started = False

    for thread in threads:
      self.thread_list.append(thread())    
 
    for thread in self.thread_list:
      while thread.is_init == False:
        delay(1)
      thread.start()

    self.is_all_thread_started = True

    cliAdd("thread", self.cliCmd)

  def __del__(self):
    for thread in self.thread_list:
      del(thread)

  def cliCmd(self, args):
    ret = False

    if len(args) == 1:
      ret = True

      if args[0] == "info":
        print("is_all_thread_started :", self.is_all_thread_started)

      elif args[0] == "list":
        print("----- Thread List -----")
        for thread in self.thread_list:
          print(thread.name)
        print("-----------------------")

      else:
        ret = False


    if ret == False:
      print("thread info")
      print("thread list")