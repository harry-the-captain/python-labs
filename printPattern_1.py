def printPattern_1(): 
	for i in range(3):
		for j in range(5): 
			if ((i == 0 and j == 2) or (i == 1 and j in [1,3]) or (i == 2 and j < 5)):
				print("*", end=' ')
			elif (i == 1 and j == 2):
				print("1", end=' ')
			else: 
				print(" ", end=' ')
		print()

printPattern_1()

#print()
