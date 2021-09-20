from piano import Piano

class Store:
	def __init__(self, list_pianos):
		self.turnover = 0
		self.list_pianos = []
		for p in list_pianos :
			if p not in self.list_pianos:
				self.list_pianos.append(p)
		self.stock_pianos = [1 for i in range(len(self.list_pianos))]
		
	#non richiesto da TP2
	def __str__(self):
		list_pianos_string = ""
		for index,p in enumerate(self.list_pianos):
			list_pianos_string += str(index) + " " + str(p) + "\n"
		return "Pianos : \n[" + list_pianos_string + "]; Stock : " + str(self.stock_pianos) + "; Turnover :" + str(self.turnover)
		
	def add(self, piano):
		if piano in self.list_pianos:
			_index_piano = self.list_pianos.index(piano) # .index() ritorna l'indice a cui si trova quel piano specifico
			self.stock_pianos[_index_piano] += 1 # ne aggiungiamo uno al buon indice
		else:			
			self.list_pianos.append(piano)
			self.stock_pianos.append(1)
	def sell(self, piano):
		try:
			_index_piano = self.list_pianos.index(piano)
			if self.stock_pianos[_index_piano] > 0:
				self.stock_pianos[_index_piano] -= 1
				self.turnover += piano.price
			else:
				raise ValueError	
		except ValueError:
			print("The piano isn't in stock.")	
	
	def inventory_value(self):
		potential_value = 0
		for index, p in enumerate(self.list_pianos): # enulerate() crea un "dizionario" (aggiunge un indice per ogni elemento di una lista)
			potential_value += p.price * self.stock_pianos[index]
		return potential_value
		
			
if __name__ == "__main__" : 
	p1 = Piano(500, "Yamaha", 2019, 100, 88)
	p2 = Piano(250, "Stylish Brand", 2020, 90, 97)
	p3 = Piano(250, "Yamaha", 2017, 90, 97)
	p4 = Piano(150, "Yamaha", 2017, 90, 97)
	list_pianos = [p1, p2, p3, p1]
	print(list_pianos)
	s1 = Store(list_pianos)
	print(s1)
	s1.sell(p1)
	print(s1)
	s1.sell(p1)
	s1.sell(p4)	
	s1.add(p4)
	s1.add(p4)
	print(s1)
	print(s1.inventory_value())
	#changed something
	
