from define import *

from serial import Serial
import serial.tools.list_ports as sp


class Uart:
  def __init__(self):
    self.uart_list:dict[str, Serial] = {}


    cliAdd("uart", self.cliCmd)

  def __del__(self):
    for uart in self.uart_list.values():
      uart.close()

  def open(self, port:str, baud:int=9600, timeout:float=None):
    if port in self.uart_list.keys():
      return True

    try:
      serial = Serial(port, baud, timeout=timeout)
      self.uart_list[port] = serial
    except:
      return False
    return True

  def close(self, port:str):  
    if port not in self.uart_list.keys():
      return False
    
    self.uart_list[port].close()
    del(self.uart_list[port])
    return True

  def isOpen(self, port:str):
    if port in self.uart_list.keys():
      return True
    return False

  def available(self, port:str):
    if port not in self.uart_list.keys():
      return False
    return self.uart_list[port].inWaiting()

  def read(self, port:str, size=1):
    if port not in self.uart_list.keys():
      return False
    return self.uart_list[port].read(size)

  def write(self, port:str, data):
    if port not in self.uart_list.keys():
      return False
    return self.uart_list[port].write(data)
      
  def flush(self, port:str):
    if port not in self.uart_list.keys():
      return False
    self.uart_list[port].flush()
    self.uart_list[port].reset_input_buffer()
    self.uart_list[port].reset_output_buffer()
    return True

  def getBaudList(self):
    return [9600, 57600, 115200, 1000000, 2000000, 4000000]

  def getPortList(self):
    return sorted(sp.comports())
  
  
  def cliCmd(self, args):
    ret = False

    if len(args) == 1:
      ret = True

      if args[0] == "info":
        print("uart list cnt :", len(self.uart_list))
      elif args[0] == "list":
        print("--- opend port list ---")
        for port in self.uart_list.keys():
          print(port)
      else:
        ret = False
    elif len(args) == 2:
      ret = True

      if args[0] == "get":
        if args[1] == "ports":
          print("--- port list ---")
          for port in self.getPortList():
            print(port)
        elif args[1] == "bauds":
          print("--- baud list ---")
          for baud in self.getBaudList():
            print(baud)
        else:
          ret = False
      elif args[0] == "close":
        port = args[1]
        self.close(port)
      elif args[0] == "available":
        port = args[1]
        available = self.available(port)
        print("available :", available)
      else:
        ret = False
    elif len(args) == 3:
      ret = True

      if args[0] == "open":
        port = args[1]
        baud = int(args[2])
        open = self.open(port, baud)
        print("Open port {0}:{1} {2}".format(port, baud, open))
      elif args[0] == "read":
        port = args[1]
        size = int(args[2])
        read = self.read(port, size)
        print("rx data :", read)
      elif args[0] == "write":
        port = args[1]
        data = bytes(args[2], encoding="utf-8")
        self.write(port, data)
      else:
        ret = False
    

    if ret == False:
      print("uart info")
      print("uart list")
      print("uart get ports")
      print("uart get bauds")
      print("uart open port[str] baud[int]")
      print("uart close port[str]")
      print("uart available port[str]")
      print("uart read port[str] size[int]")
      print("uart write port[str] data")
      