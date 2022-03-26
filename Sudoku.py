import numpy as np

# every list within the list reperesnt a row
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]

print("\nThe matrix that is needed to be solved is this one\n")

print(np.matrix(grid)) # to print the unsolved matrix

print("\nThe solved version of this matrix are as follows\n")

def possible(row, column, number):

	global grid 

	# To check if the number is present in that row

	for i in range(0,9):
		if grid[row][i] == number:
			return False



	# To check if the number is present in that column

		if grid[i][column] == number:
			return False  
	

	# To check if the number is present in that sqaure

	x0 = (column // 3) * 3
	y0 = (row // 3) * 3
	for i in range(0,3):
		for j in range(0,3):
			if grid[y0+i][x0+j] == number:
				return False

	return True

def sudokuSolve():
	global grid
	for row in range(0,9):
		for column in range(0,9):
			if grid[row][column] == 0:
				for number in range(1,10):
					if possible(row,column,number):
						grid[row][column] = number
						sudokuSolve()
						grid[row][column] = 0

				return 

	print(np.matrix(grid)) # to print the solved matrix

	raw_input('\nMore possible solutions of this matrix. Hit Enter to see them\n')


sudokuSolve()

