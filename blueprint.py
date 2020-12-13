from reader import reader
import struct
import zlib
import json

class blueprint:
	def __init__(self, path, pcDir):

		self.pcDir = pcDir
		self.injectionPoint = "{}/Blueprints/Tracks/AethonBlueprint01.blueprint".format(self.pcDir)

		self.dataPath = path + "/fcompressedsave_blueprint"
		self.data = open(self.dataPath, "rb").read()
		self.data = self.deflateE(self.data)
		self.data = self.data[16:]
		self.dataReader = reader(self.data)

		self.metaPath = path + "/fcompressedsave_metadata"
		self.metaData = open(str(self.metaPath), "rb").read()
		self.metaData = self.deflateE(self.metaData)
		self.metaData = self.metaData[16:]
		self.metaJson = json.loads(self.metaData)

		self.name = self.metaJson["sName"]

		self.header = self.dataReader.ReadBytes(11)
		self.version = self.dataReader.ReadBytes(15)
		self.steam = self.dataReader.ReadBytes(7)
		self.unknown = self.dataReader.ReadBytes(1)
		self.unknown2 = self.dataReader.ReadBytes(40)
		self.unknown3 = self.dataReader.ReadBytes(2)
		self.stringHeader = self.dataReader.ReadBytes(8)
		self.stringsCount = self.dataReader.ReadNum(1)
		self.stringsPos = self.dataReader.pointer

		self.strings = []
		self.stringLength = 0

		for i in range(self.stringsCount):
			self.string = ""
			while True:
				self.char = self.dataReader.ReadBytes(1)
				if int.from_bytes(self.char,"little", signed=False) != 0:
					try:
						self.string = self.string + self.char.decode("utf-8")
					except:
						pass
				else:
					self.strings.append(self.string)
					self.stringLength += len(self.string)
					break

		self.endPos = self.dataReader.pointer

	def readHeader(self):
		pass

	def deflateE(self, data):
		self.decompress = zlib.decompressobj(-15)
		return (self.decompress.decompress(data))

	def write_strings(self, edit, pcdir):
		self.pcDir = pcdir
		self.injectionPoint = "{}/Blueprints/Tracks/AethonBlueprint01.blueprint".format(self.pcDir)
		out = str.encode(">") + str.encode(chr(len(self.strings))) + b'\xf3' + str.encode(edit[0])
		for item in range(1, self.stringsCount):
			#print("Item {}, Length {}, Item {}".format(item, self.stringsCount, self.strings[item]))
			out = out + str.encode(chr(0)) + b'\xf3' + str.encode(edit[item])

		a = self.data[:self.stringsPos-2]
		a = a + out
		b = self.data[self.endPos-1 : ]
		a = a + b

		open(self.injectionPoint,"wb").write(a)
		#print(self.strings)
