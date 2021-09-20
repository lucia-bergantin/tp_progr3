from instrument import Instrument
import math

class Piano(Instrument):
	def __init__(self, price, brand, year, volume, number_of_keys):
		super().__init__(price, brand, year, volume)
		self.number_of_keys = number_of_keys

	def __str__(self):
		return super().__str__() + "; Number of keys : " + str(self.number_of_keys)
		
	#non richiesto da TP2
	def __eq__(self, p2):
		return super().__eq__(p2) and self.number_of_keys == p2.number_of_keys
		
	
	def muted_volume(self):
		return math.sqrt(self.volume)
		
		
if __name__ == "__main__" : 
	p1 = Piano(500, "Yamaha", 2019, 100, 88)
	p2 = Piano(250, "Stylish Brand", 2020, 90, 97)
	
	#non richiesto da TP2
	print(p1 == p1)
	print(p1 == p2)
	
	print(p1, "\n", p2)
	print(p1.muted_volume(), p2.muted_volume())	

