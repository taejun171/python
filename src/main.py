import sys
from os import path
from PySide6.QtWidgets import QApplication

sys.path.append(path.dirname( path.dirname( path.abspath(__file__) ) ))

from define import *
from thread.thread import Thread




def main():
  app = QApplication(sys.argv)

  print("python project")

  thread_manager = Thread()

  sys.exit(app.exec())


if __name__ == "__main__":  
  main()