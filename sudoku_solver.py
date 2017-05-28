from collections import deque
sudoku = []
def read_inp():
	global sudoku
	inp = '52...6.........7.13...........4..8..6......5...........418.........3..2...87.....'
	index = 1
	row = []
	for c in inp:
		if c == '.':
			deq = deque()
			deq.append(0)
			row.append(deq)
		else:
			deq = deque()
			deq.append(int(c))
			deq.append(10)
			row.append(deq)
			#row.append([int(c), 10])
		if index >= 9:
			sudoku.append(row)
			row =[]
			index = 0
		index += 1
	print(sudoku)


# row1 = [[0],[0],[3,10],[6,10],[0],[0],[9,10],[0],[5,10]]
# row2 = [[2,10],[0],[0],[0],[5,10],[0],[0],[0],[0]]
# row3 = [[0],[0],[4,10],[2,10],[0],[0],[0],[0],[0]]
# row4 = [[8,10],[0],[0],[0],[0],[2,10],[0],[7,10],[0]]
# row5 = [[0],[0],[5,10],[7,10],[3,10],[8,10],[2,10],[0],[0]]
# row6 = [[0],[7,10],[0],[5,10],[0],[0],[0],[0],[8,10]]
# row7 = [[0],[0],[0],[0],[0],[3,10],[7,10],[0],[0]]
# row8 = [[0],[0],[0],[0],[6,10],[0],[0],[0],[9,10]]
# row9 = [[3,10],[0],[6,10],[0],[0],[5,10],[1,10],[0],[0]]


# sudoku = [row1,row2,row3,row4,row5,row6,row7,row8,row9]

# import sys
# sys.setrecursionlimit(3500)
# 0th element will always hold current value
def print_sudoku():
	for row in sudoku:
		new_row = []
		for col in row:
			new_row.append(col[0])
		print(new_row)

def get_row_values(current_row_index, current_col_index):
	col = 0
	row_values = []
	while col<9:
		row_values.append(sudoku[current_row_index][col][0])
		col += 1
	return row_values

def get_column_values(current_row_index, current_col_index):
	row = 0
	col_values = []
	while row < 9:
		col_values.append(sudoku[row][current_col_index][0])
		row += 1
	return col_values
	
def get_grid_values(current_row_index, current_col_index):
	values = []
	if current_row_index <3 and current_col_index < 3:
		row = 0
		while row < 3:
			col = 0
			while col < 3:
				values.append(sudoku[row][col][0])
				col += 1
			row +=1
	if current_row_index >=3 and current_row_index < 6 and current_col_index < 3:
		row = 3
		while row < 6:
			col = 0
			while col < 3:
				values.append(sudoku[row][col][0])
				col += 1
			row +=1	
	if current_row_index >=6 and current_col_index < 3:
		row = 6
		while row < 9:
			col = 0
			while col < 3:
				values.append(sudoku[row][col][0])
				col += 1
			row +=1	
	if current_row_index < 3 and current_col_index >= 3 and current_col_index < 6:
		row = 0
		while row < 3:
			col = 3
			while col < 6:
				values.append(sudoku[row][col][0])
				col += 1
			row +=1	
	if current_row_index >=3 and current_row_index < 6 and current_col_index >= 3 and current_col_index < 6:
		row = 3
		while row < 6:
			col = 3
			while col < 6:
				values.append(sudoku[row][col][0])
				col += 1
			row +=1	
	if current_row_index >=6 and current_col_index >= 3 and current_col_index < 6:
		row = 6
		while row < 9:
			col = 3
			while col < 6:
				values.append(sudoku[row][col][0])
				col += 1
			row +=1	
	if current_row_index <3 and current_col_index >= 6:
		row = 0
		while row < 3:
			col = 6
			while col < 9:
				values.append(sudoku[row][col][0])
				col += 1
			row +=1
	if current_row_index >=3 and current_row_index < 6 and current_col_index >= 6:
		row = 3
		while row < 6:
			col = 6
			while col < 9:
				values.append(sudoku[row][col][0])
				col += 1
			row +=1
	if current_row_index >=6 and current_col_index >= 6:
		row = 6
		while row < 9:
			col = 6
			while col < 9:
				values.append(sudoku[row][col][0])
				col += 1
			row +=1

	return values

def solve_sudoku():
	going_back = False
	current_row = 0
	current_col = 0
	while current_row<=8 and current_col <=8:
		if sudoku[current_row][current_col][len(sudoku[current_row][current_col])-1] == 10:
		#already fixed value, move to next 
			if going_back:
				if current_col <= 0:
					current_row -= 1
					current_col = 8
				else:
					current_col -= 1
			else:
				if current_col>=8:
					current_row = current_row + 1
					current_col = 0
				else:
					current_col += 1
			continue
		#already_taken = []
		already_taken = {}
		val = 0
		for val in get_row_values(current_row, current_col):
			already_taken[val] = 1
		for val in get_column_values(current_row, current_col):
			already_taken[val] = 1
		for val in get_grid_values(current_row, current_col):
			already_taken[val] = 1
		for val in sudoku[current_row][current_col]:
			already_taken[val] = 1
		# already_taken.append(get_column_values(current_row, current_col))
		# already_taken.append(get_grid_values(current_row, current_col))
		# already_taken.append(sudoku[current_row][current_col])

		#print(already_taken)
		not_already_taken = 10

		i = 1
		while i < 10:
			if already_taken.get(i):
				i += 1
			else:
				not_already_taken = i
				break
				
		if not_already_taken ==10:
			#all values are taken change previous values
			deq = deque()
			deq.append(0)
			sudoku[current_row][current_col]=deq
			if current_col == 0 and current_row == 0:
				print('sudoku cannot be solved')
				break
			elif current_col <= 0:
				current_row -= 1
				current_col = 8
			else:
				current_col -= 1
			going_back = True
		else:
			sudoku[current_row][current_col].appendleft(not_already_taken)
			#print(str(current_row) + ' - ' + str(current_col) + ' : ' + str(sudoku[current_row][current_col]))
			if current_col>=8:
				current_row += 1
				current_col = 0
			else:
				current_col += 1
			going_back = False

# sudoku_solved = False
# def solve_sudoku(current_row, current_col):
# 	global sudoku_solved
# 	if sudoku_solved:
# 		return
# 	if current_row >=8 and current_col >=8:
# 		sudoku_solved = True
# 		return

# 	if sudoku[current_row][current_col][len(sudoku[current_row][current_col])-1] == 10:
# 		#already fixed value, move to next 
# 		if current_col>=8:
# 			solve_sudoku(current_row + 1, 0)
# 		else:
# 			solve_sudoku(current_row, current_col + 1)
# 		return
# 	already_taken = []
# 	val = 0
# 	for val in get_row_values(current_row, current_col):
# 		already_taken.append(val)
# 	for val in get_column_values(current_row, current_col):
# 		already_taken.append(val)
# 	for val in get_grid_values(current_row, current_col):
# 		already_taken.append(val)
# 	for val in sudoku[current_row][current_col]:
# 		already_taken.append(val)
# 	# already_taken.append(get_column_values(current_row, current_col))
# 	# already_taken.append(get_grid_values(current_row, current_col))
# 	# already_taken.append(sudoku[current_row][current_col])

# 	#print(already_taken)
# 	not_already_taken = 10

# 	i = 1
# 	while i < 10:
# 		if i not in already_taken:
# 			not_already_taken = i
# 			break
# 		else:
# 			i += 1
# 	if not_already_taken ==10:
# 		#all values are taken change previous values
# 		sudoku[current_row][current_col]=[0]
# 		if current_col == 0 and current_row == 0:
# 			print('sudoku cannot be solved')
# 			sudoku_solved = True
# 			return
# 		elif current_col <= 0:
# 			solve_sudoku(current_row-1, 8)
# 		else:
# 			solve_sudoku(current_row, current_col - 1)
# 	else:
# 		sudoku[current_row][current_col].insert(0, not_already_taken)
# 		if current_col>=8:
# 			solve_sudoku(current_row + 1, 0)
# 		else:
# 			solve_sudoku(current_row, current_col + 1)
if __name__=='__main__':
	read_inp()
	print_sudoku()
	#print(get_grid_values(2,2))
	solve_sudoku()

	print()

	print_sudoku()
#basic algo
# update for sudoku set of values each cell can take, keep hold of cell requiring set of  lowest values
# update its value and check if

 