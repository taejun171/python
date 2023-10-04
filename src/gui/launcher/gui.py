from .ui.ui import *




class LauncherGui(QMainWindow):
  def __init__(self):
    super(LauncherGui, self).__init__()
    self.is_init = False
    self.name = "Launcher"
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)


    self.is_init = True

  def __del__(self):
    pass

  def closeEvent(self, QCloseEvent):
    pass