
import sys
import pickle

import PySide6.QtGui

from ui.ui import *
from PySide6.QtWidgets import QAbstractItemView, QStyledItemDelegate

from driver.uart import *
from lib.protocol_handler import *


class NonEditableDelegate(QStyledItemDelegate):
  def createEditor(self, _parent, _option, _index):
    return None


class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.ui = Ui_Launcher()
    self.ui.setupUi(self)

    self.setClickEvent(self.ui.pb_scan,    self.btnScan)
    self.setClickEvent(self.ui.pb_connect, self.btnConnect)
    self.setClickEvent(self.ui.pb_clear,   self.btnClear)

    self.ui.lw_protocol_list.itemSelectionChanged.connect(self.protocolSelected)
    self.ui.tw_object_explorer.itemSelectionChanged.connect(self.objectSelected)
    self.ui.tw_attribute_editor.itemChanged.connect(self.attributeChanged)

    self.ui.tw_attribute_editor.setItemDelegateForColumn(0, NonEditableDelegate())

    self.setContextMenu(self.ui.lw_protocol_list)
    self.setContextMenu(self.ui.tw_object_explorer)
    self.setContextMenu(self.ui.tw_attribute_editor)

    self.action_list = []
    self.createAction("&New",    self.actNew, "Ctrl+N")
    self.createAction("&Delete", self.actDel, "Delete")

    self.uart = Uart()
    self.uart.rxd_thread.setEnableThread(False)

    self.protocol_selected:QListWidgetItem = None
    self.object_selected:QTreeWidgetItem   = None

    self.btnScan()

  def __del__(self):
    pass

  def closeEvent(self, QCloseEvent):
    self.uart.close()
    pass

  def setClickEvent(self, event_dst, event_func):
    event_dst.clicked.connect(lambda: self.btnClicked(event_dst, event_func))

  def btnClicked(self, button, event_func):
    event_func()

  def createAction(self, text:str, func, shortcut:str=None):
    action = QAction(text)
    if shortcut != None:
      action.setShortcut(shortcut)
    self.action_list.append([action, func])

  def setContextMenu(self, event_dst):
    event_dst.setContextMenuPolicy(Qt.CustomContextMenu)
    event_dst.customContextMenuRequested.connect(lambda: self.showContextMenu(event_dst))

  def showContextMenu(self, obj):
    menu = QMenu(obj)
    for action, func in self.action_list:
      menu.addAction(action)
    act = menu.exec(QCursor.pos())
    for action, func in self.action_list:
      if act == action:
        func(obj)

  def protocolSelected(self):
    self.protocol_selected = None

    items = self.ui.lw_protocol_list.selectedItems()
    if len(items) > 0:
      for item in items:
        self.protocol_selected = item

    self.showSelectedProtocol(self.protocol_selected)

  def objectSelected(self):
    self.object_selected = None

    items = self.ui.tw_object_explorer.selectedItems()
    if len(items) > 0:
      for item in items:
        self.object_selected = item

    self.showObjectAttribute(self.object_selected)
    
  def attributeChanged(self, item:QTreeWidgetItem, column:int):
    object_type = self.object_selected.text(1)
    attr_str = item.text(0)
    protocol:Protocol = self.protocol_selected.data(Qt.UserRole)
    packet = protocol.getPacket(self.object_selected.text(0))

    if object_type == "Packet":
      packet = protocol.getPacket(self.object_selected.text(0))
      if attr_str == "name":
        packet.name = item.text(column)
        self.object_selected.setText(0, item.text(column))

    elif object_type == "Field":
      packet = protocol.getPacket(self.object_selected.parent().text(0))
      field = packet.getField(self.object_selected.text(0))
      if attr_str == "name":
        field.name = item.text(column)
        self.object_selected.setText(0, item.text(column))
      else:
        field.getAttribute(attr_str).setValue(item.text(column))
      



  def actNew(self, obj):
    if obj == self.ui.lw_protocol_list:
      protocol = Protocol("new_protocol")
      item = QListWidgetItem(protocol.name)
      item.setFlags(item.flags() | Qt.ItemIsEditable)
      item.setData(Qt.UserRole, protocol)
      self.ui.lw_protocol_list.addItem(item)
      
    elif obj == self.ui.tw_object_explorer:
      if self.protocol_selected != None:
        protocol:Protocol = self.protocol_selected.data(Qt.UserRole)
        if self.object_selected == None:
          protocol.appendPacket("new_packet")
        elif self.object_selected.text(1) == "Packet":
          packet = protocol.getPacket(self.object_selected.text(0))
          packet.appendField("new_field")
      self.showSelectedProtocol(self.protocol_selected)
        
    elif obj == self.ui.tw_attribute_editor:
      pass

  def actDel(self, obj):
    if obj == self.ui.lw_protocol_list:
      for protocol in self.ui.lw_protocol_list.selectedItems():
        self.ui.lw_protocol_list.takeItem(self.ui.lw_protocol_list.row(protocol))
    elif obj == self.ui.tw_object_explorer:
      if self.protocol_selected != None and self.object_selected != None:
        protocol:Protocol = self.protocol_selected.data(Qt.UserRole)
        object_type = self.object_selected.text(1)
        if object_type == "Packet":
          ret = protocol.delPacket(self.object_selected.text(0))
        elif object_type == "Field":
          packet = protocol.getPacket(self.object_selected.parent().text(0))
          ret = packet.delField(self.object_selected.text(0))
      self.showSelectedProtocol(self.protocol_selected)
          
    elif obj == self.ui.tw_attribute_editor:
      pass



  def btnScan(self):
    self.ui.cb_port.clear()
    self.ui.cb_baud.clear()

    for port in self.uart.getPortList():
      self.ui.cb_port.addItem(port.device)      
      self.ui.cb_port.setItemData(self.ui.cb_port.count()-1, port.manufacturer + ' ' + port.description, Qt.ToolTipRole)

    bauds = self.uart.getBaudList()
    self.ui.cb_baud.addItems([str(i) for i in bauds])

    if self.ui.cb_port.count() > 0:
      self.ui.pb_connect.setEnabled(True)
    else:
      self.ui.pb_connect.setEnabled(False)

  def btnConnect(self):
    port = self.ui.cb_port.currentText()
    baud = int(self.ui.cb_baud.currentText())

    if self.uart.isOpen() == True:
      self.uart.close()
      self.ui.pb_connect.setText("Connect")
      self.ui.cb_port.setEnabled(True)
      self.ui.cb_baud.setEnabled(True)
      self.ui.pb_scan.setEnabled(True)
    else:
      if self.uart.open(port, baud) == True:
        self.ui.pb_connect.setText("Disconnect")
        self.ui.cb_port.setEnabled(False)
        self.ui.cb_baud.setEnabled(False)
        self.ui.pb_scan.setEnabled(False)
    

  def btnClear(self):
    self.ui.tw_packet_log.clear()
    self.ui.pte_raw.clear()

  def loadItems(self):
    try :
      file = open('items.ptl', 'rb')
      return pickle.load(file)
    except:
      return []

  def saveItems(self, items):
    try :
      file = open('items.ptl', 'wb')
      pickle.dump(items, file)
      return True
    except:
      return False
    
  def showSelectedProtocol(self, item_protocol:QListWidgetItem):
    self.ui.tw_object_explorer.clear()
    if item_protocol == None:
      return
    protocol:Protocol = item_protocol.data(Qt.UserRole)
    items = []

    for packet in protocol.getPackets():
      item_packet = QTreeWidgetItem([packet.name, protocolGetObjectName(packet)])
      item_packet.setExpanded(True)

      for field in packet.getFields():
        item_field = QTreeWidgetItem([field.name, protocolGetObjectName(field)])
        item_field.setExpanded(True)
        item_packet.addChild(item_field)

      items.append(item_packet)
    
    self.ui.tw_object_explorer.insertTopLevelItems(0, items)
    self.ui.tw_object_explorer.expandAll()

  def showObjectAttribute(self, item_object:QTreeWidgetItem):
    self.ui.tw_attribute_editor.clear()
    if item_object == None:
      return
    object_type = item_object.text(1)
    protocol:Protocol = self.protocol_selected.data(Qt.UserRole)
    items = []

    if object_type == "Packet":
      packet = protocol.getPacket(item_object.text(0))
      item = QTreeWidgetItem(["name", packet.name])
      items.append(item)
    elif object_type == "Field":
      packet = protocol.getPacket(self.object_selected.parent().text(0))
      field = packet.getField(item_object.text(0))

      item = QTreeWidgetItem(["name", field.name])
      items.append(item)

      for attr in field.getAttributes():
        item = QTreeWidgetItem([attr.name, attr.value])
        items.append(item)

    for item in items:
      item.setFlags(item.flags() | Qt.ItemIsEditable)

    self.ui.tw_attribute_editor.insertTopLevelItems(0, items)


def mainApp():
  window = MainWindow()
  window.show()
  window.initUi()


def main():
  app = QApplication(sys.argv)

  window = MainWindow()
  window.show()

  sys.exit(app.exec())


if __name__ == "__main__":  
  main()
  