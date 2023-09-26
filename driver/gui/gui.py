import PySide6.QtGui

from .ui.ui import *





class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.ui = Ui_Launcher()
    self.ui.setupUi(self)

  def __del__(self):
    pass