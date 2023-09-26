DEFAULT_MAX_BUFFER_SIZE = 1024

ATTR_SIZE_FIXED = "size_fixed"
ATTR_SIZE_VALUE = "size_value"
ATTR_DATA_FIXED = "data_fixed"
ATTR_DATA_VALUE = "data_value"


def protocolGetObjectName(object)->str:
  str = ""
  object_type = type(object)
  if object_type == Protocol:
    str = "Protocol"
  elif object_type == Packet:
    str = "Packet"
  elif object_type == Field:
    str = "Field"
  elif object_type == Attribute:
    str = "Attribute"

  return str

class Attribute:
  def __init__(self, name:str=""):
    self.name:str = name
    self.value = None

  def getValue(self):
    return self.value
  
  def setValue(self, value):
    self.value = value


class Field:
  def __init__(self, name:str=""):
    self.name:str = name
    self.attributes:list[Attribute] = []
    self.data = []

    # default attributes
    self.appendAttribute(ATTR_SIZE_FIXED)
    self.appendAttribute(ATTR_SIZE_VALUE)
    self.appendAttribute(ATTR_DATA_FIXED)
    self.appendAttribute(ATTR_DATA_VALUE)

  def getAttribute(self, name:str)->Attribute:
    for attribute in self.attributes:
      if name == attribute.name:
        return attribute
    return None

  def appendAttribute(self, name:str)->bool:
    for attribute in self.attributes:
      if name == attribute.name:
        return False
    self.attributes.append(Attribute(name))
    return True

  def delAttribute(self, name:str)->bool:
    for attribute in self.attributes:
      if name == attribute.name:
        self.attributes.remove(attribute)
        return True
    return False
    
  def getAttributes(self):
    for attribute in self.attributes:
      yield attribute
  
  def getAttributesStr(self):
    for attribute in self.attributes:
      yield attribute.name
  
  def getData(self)->list:
    return self.data
  
  def setData(self, data:list):
    self.data = data

  def isData(self)->bool:
    if len(self.data) > 0:
      return True
    return False


class Packet:
  def __init__(self, name:str=""):
    self.name:str = name
    self.fields:list[Field] = []
    self.buffer = []

  def getField(self, name:str)->Field:
    for field in self.fields:
      if name == field.name:
        return field
    return None

  def appendField(self, name:str)->bool:
    for field in self.fields:
      if name == field.name:
        return False
    self.fields.append(Field(name))
    return True

  def delField(self, name:str)->bool:
    for field in self.fields:
      if name == field.name:
        self.fields.remove(field)
        return True
    return False
    
  def getFields(self):
    for field in self.fields:
      yield field
  
  def getFieldsStr(self):
    for field in self.fields:
      yield field.name

  def getData(self)->list:
    data = []
    for field in self.getFields():
      data.extend(field.getData())
    return data
  
  def clearData(self):
    for field in self.getFields():
      field.setData([])

  def isAllData(self)->bool:
    for field in self.getFields():
      if field.isData() == False:
        return False
    return True
  
  def getBuffer(self)->list:
    return self.buffer
  

class Protocol:
  def __init__(self, name:str=""):
    self.packets:list[Packet] = []
    self.name:str = name

  def getPacket(self, name:str)->Packet:
    for packet in self.packets:
      if name == packet.name:
        return packet
    return None
    
  def appendPacket(self, name:str)->bool:
    for packet in self.packets:
      if name == packet.name:
        return False
    self.packets.append(Packet(name))
    return True

  def delPacket(self, name:str)->bool:
    for packet in self.packets:
      if name == packet.name:
        self.packets.remove(packet)
        return True
    return False
    
  def getPackets(self):
    for packet in self.packets:
      yield packet
  
  def getPacketsStr(self):
    for packet in self.packets:
      yield packet.name


class ProtocolHandler:
  def __init__(self, protocol:Protocol):
    self.protocol = protocol
    self.data = []
    self.max_buffer_size = DEFAULT_MAX_BUFFER_SIZE

  def __del__(self):
    pass

  def __getSizeValue(self, packet:Packet, size_value:str)->int:
    '''
    convert operation string to size value
    '''

    for field in packet.getFields():
      field_data = int.from_bytes(field.getData(), "little")
      size_value = size_value.replace(field.name, str(field_data))

    return eval(size_value)

  def __getDataValue(self, packet:Packet, size:int, data_value:str)->list:
    '''
    convert operation string to data value
    '''

    for field in packet.getFields():
      field_data = int.from_bytes(field.getData(), "little")
      data_value = data_value.replace(field.name, str(field_data))

    return eval(data_value).to_bytes(size, byteorder = 'little')
  
  def setMaxBufferSize(self, size=DEFAULT_MAX_BUFFER_SIZE):
    self.max_buffer_size = size

  def process(self, data)->list:
    '''
    return list of [packet Str, data]
    '''
    data_ret = []

    for packet in self.protocol.getPackets():
      data_buf = packet.getBuffer()
      data_buf.append(data)

      if len(data_buf) > self.max_buffer_size:
        data_buf.pop(0)

      for field in packet.getFields():
        if field.isData() == False:
          size_fixed = field.getAttribute(ATTR_SIZE_FIXED).getValue()
          size_value = field.getAttribute(ATTR_SIZE_VALUE).getValue()
          data_fixed = field.getAttribute(ATTR_DATA_FIXED).getValue()
          data_value = field.getAttribute(ATTR_DATA_VALUE).getValue()

          if size_fixed == False:
            size_value = self.__getSizeValue(packet, size_value)
          if data_fixed == False and data_value != None:
            data_value = self.__getDataValue(packet, size_value, data_value)

          if len(data_buf) >= size_value:
            data_compare = data_buf[-size_value:]

            if data_value == None or data_compare == data_value:
              field.setData(data_compare)
              data_buf.clear()
            else:
              break
          break

      if packet.isAllData() == True:
        data_ret.append([packet.name, packet.getData()])
        packet.clearData()

    return data_ret