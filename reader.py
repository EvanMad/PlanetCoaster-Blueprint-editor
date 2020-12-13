class reader:
	def __init__(self, data):
		self.data = data
		self.pointer = 0
	def ReadByte(self):
		output = self.data[self.pointer]
		self.pointer += 1
		return output
	def ReadBytes(self,byteCount):
		output = self.data[self.pointer: self.pointer+byteCount]
		self.pointer += byteCount
		return output
	def ReadUInt(self):
		output = self.data[self.pointer: self.pointer+4]
		self.pointer += 4
		#return output
		return (int.from_bytes(output,"little", signed=False))
	def ReadUInt8(self):
		output = self.data[self.pointer: self.pointer + 8]
		self.pointer += 8
		return (int.from_bytes(output, "little", signed=False))
	def ReadUShort(self):
		output = self.data[self.pointer: self.pointer+2]
		self.pointer += 2
		return (int.from_bytes(output,"little", signed=False))
	def ReadString(self, length):
		output = self.data[self.pointer: self.pointer + length]
		self.pointer += length
		return (output.decode("utf-8"))
	def ReadNum(self,length):
		output = self.data[self.pointer: self.pointer + length]
		self.pointer += length
		return int.from_bytes(output,"little", signed=False)

	def setPointer(self, pos):
		self.pointer = pos
