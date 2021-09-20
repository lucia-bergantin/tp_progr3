import datetime

class Instrument:
	def __init__(self, price, brand, year, volume):
		self.price = price
		self.brand = brand
		self.year = year
		self.volume = volume
	def __str__(self):
		return "Price : " + str(self.price) + "; Brand : " + self.brand + "; Year of creation : " + str(self.year) + "; Volume : " + str(self.volume)

	def __eq__(self, i2):
		return self.price == i2.price and self.brand == i2.brand and self.year == i2.year and self.volume == i2.volume		
		
	def is_new(self):	
		return self.year == datetime.datetime.now().year

if __name__ == "__main__" : 
	instr1 = Instrument(500, "Yamaha", 2019, 100)
	instr2 = Instrument(250, "Stylish Brand", 2021, 90)
	
	print(instr2)
	print(instr2 == instr1)
	print(instr1 == instr1)
	print(instr1.is_new(), instr2.is_new())	

