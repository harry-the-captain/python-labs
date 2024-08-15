def printPattern_2():
	for i in range(0,6):
		for j in range(0,7):
			if ((i == 0 and j == 3) or (i in [1,3] and j in [2,4]) or (i == 2 and j in [1,5]) or (i in [4,5] and j < 7)):
				print("*", end=' ')
			elif (i == 2 and j == 3):
				print("2", end=' ')
			else: 
				print(" ", end=' ')
				
		print()
		
printPattern_2()
