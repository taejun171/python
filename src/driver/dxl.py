from lib.protocol_handler import *

PACKET_STATUS     = "status"
PACKET_INSTUCTION = "instuction"

FIELD_HEADER      = "header"
FIELD_RESERVED    = "reserved"
FIELD_ID          = "id"
FIELD_LENGTH      = "length"
FIELD_INSTRUCTION = "instruction"
FIELD_ERROR       = "error"
FIELD_PARAM       = "param"
FIELD_CRC         = "crc"


class Dxl:
  def __init__(self):
    self.dxl = Protocol("dxl")
    self.dxl.appendPacket(PACKET_STATUS)

    self.dxl.getPacket(PACKET_STATUS).appendField(FIELD_HEADER)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_HEADER).getAttribute(ATTR_SIZE_FIXED).setValue(True)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_HEADER).getAttribute(ATTR_SIZE_VALUE).setValue(3)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_HEADER).getAttribute(ATTR_DATA_FIXED).setValue(True)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_HEADER).getAttribute(ATTR_DATA_VALUE).setValue([0xFF, 0xFF, 0xFD])

    self.dxl.getPacket(PACKET_STATUS).appendField(FIELD_RESERVED)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_RESERVED).getAttribute(ATTR_SIZE_FIXED).setValue(True)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_RESERVED).getAttribute(ATTR_SIZE_VALUE).setValue(1)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_RESERVED).getAttribute(ATTR_DATA_FIXED).setValue(True)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_RESERVED).getAttribute(ATTR_DATA_VALUE).setValue([0x00])

    self.dxl.getPacket(PACKET_STATUS).appendField(FIELD_ID)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_ID).getAttribute(ATTR_SIZE_FIXED).setValue(True)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_ID).getAttribute(ATTR_SIZE_VALUE).setValue(1)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_ID).getAttribute(ATTR_DATA_FIXED).setValue(False)

    self.dxl.getPacket(PACKET_STATUS).appendField(FIELD_LENGTH)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_LENGTH).getAttribute(ATTR_SIZE_FIXED).setValue(True)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_LENGTH).getAttribute(ATTR_SIZE_VALUE).setValue(2)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_LENGTH).getAttribute(ATTR_DATA_FIXED).setValue(False)

    self.dxl.getPacket(PACKET_STATUS).appendField(FIELD_INSTRUCTION)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_INSTRUCTION).getAttribute(ATTR_SIZE_FIXED).setValue(True)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_INSTRUCTION).getAttribute(ATTR_SIZE_VALUE).setValue(1)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_INSTRUCTION).getAttribute(ATTR_DATA_FIXED).setValue(True)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_INSTRUCTION).getAttribute(ATTR_DATA_VALUE).setValue([0x55])

    self.dxl.getPacket(PACKET_STATUS).appendField(FIELD_ERROR)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_ERROR).getAttribute(ATTR_SIZE_FIXED).setValue(True)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_ERROR).getAttribute(ATTR_SIZE_VALUE).setValue(1)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_ERROR).getAttribute(ATTR_DATA_FIXED).setValue(False)

    self.dxl.getPacket(PACKET_STATUS).appendField(FIELD_PARAM)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_PARAM).getAttribute(ATTR_SIZE_FIXED).setValue(False)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_PARAM).getAttribute(ATTR_SIZE_VALUE).setValue("length-4")
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_PARAM).getAttribute(ATTR_DATA_FIXED).setValue(False)

    self.dxl.getPacket(PACKET_STATUS).appendField(FIELD_CRC)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_CRC).getAttribute(ATTR_SIZE_FIXED).setValue(True)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_CRC).getAttribute(ATTR_SIZE_VALUE).setValue(2)
    self.dxl.getPacket(PACKET_STATUS).getField(FIELD_CRC).getAttribute(ATTR_DATA_FIXED).setValue(False)


    self.dxl.appendPacket(PACKET_INSTUCTION)

    self.dxl.getPacket(PACKET_INSTUCTION).appendField(FIELD_HEADER)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_HEADER).getAttribute(ATTR_SIZE_FIXED).setValue(True)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_HEADER).getAttribute(ATTR_SIZE_VALUE).setValue(3)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_HEADER).getAttribute(ATTR_DATA_FIXED).setValue(True)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_HEADER).getAttribute(ATTR_DATA_VALUE).setValue([0xFF, 0xFF, 0xFD])

    self.dxl.getPacket(PACKET_INSTUCTION).appendField(FIELD_RESERVED)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_RESERVED).getAttribute(ATTR_SIZE_FIXED).setValue(True)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_RESERVED).getAttribute(ATTR_SIZE_VALUE).setValue(1)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_RESERVED).getAttribute(ATTR_DATA_FIXED).setValue(True)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_RESERVED).getAttribute(ATTR_DATA_VALUE).setValue([0x00])

    self.dxl.getPacket(PACKET_INSTUCTION).appendField(FIELD_ID)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_ID).getAttribute(ATTR_SIZE_FIXED).setValue(True)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_ID).getAttribute(ATTR_SIZE_VALUE).setValue(1)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_ID).getAttribute(ATTR_DATA_FIXED).setValue(False)

    self.dxl.getPacket(PACKET_INSTUCTION).appendField(FIELD_LENGTH)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_LENGTH).getAttribute(ATTR_SIZE_FIXED).setValue(True)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_LENGTH).getAttribute(ATTR_SIZE_VALUE).setValue(2)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_LENGTH).getAttribute(ATTR_DATA_FIXED).setValue(False)

    self.dxl.getPacket(PACKET_INSTUCTION).appendField(FIELD_INSTRUCTION)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_INSTRUCTION).getAttribute(ATTR_SIZE_FIXED).setValue(True)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_INSTRUCTION).getAttribute(ATTR_SIZE_VALUE).setValue(1)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_INSTRUCTION).getAttribute(ATTR_DATA_FIXED).setValue(False)

    self.dxl.getPacket(PACKET_INSTUCTION).appendField(FIELD_PARAM)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_PARAM).getAttribute(ATTR_SIZE_FIXED).setValue(False)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_PARAM).getAttribute(ATTR_SIZE_VALUE).setValue("length-3")
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_PARAM).getAttribute(ATTR_DATA_FIXED).setValue(False)

    self.dxl.getPacket(PACKET_INSTUCTION).appendField(FIELD_CRC)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_CRC).getAttribute(ATTR_SIZE_FIXED).setValue(True)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_CRC).getAttribute(ATTR_SIZE_VALUE).setValue(2)
    self.dxl.getPacket(PACKET_INSTUCTION).getField(FIELD_CRC).getAttribute(ATTR_DATA_FIXED).setValue(False)

    self.handler = ProtocolHandler(self.dxl)

  def __del__(self):
    pass

  def process(self, data):
    return self.handler.process(data)