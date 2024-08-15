def printPattern_3(): 
	for i in range(0,9):
		for j in range(0,9): 
			if((i == 0 and j == 4) or (i in [1,5] and j in [3,5]) or (i in [2,4] and j in [2,6]) or (i == 3 and j in [1,7]) or (i in [6,7,8] and j < 9)):
				print("*", end=' ')
			elif (i == 3 and j == 4):
				print("3", end=' ')
			else: 
				print(" ", end=' ')
				
		print()
		
printPattern_3()
