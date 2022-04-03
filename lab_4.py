from random import randint

def print_matrix(matrix: list):
	for row in matrix:
		print(' '.join(map(str,row)))
	print()

def print_matrix_with_critical_path(matrix: list, critical_path: list):
	for i, row in enumerate(matrix):
		for j, time in enumerate(row):
			if [i, j] in critical_path:
				print("\033[30m\033[47m{}\033[0m".format(time), end=' ')
			else: 
				print(time, end=' ')
		print()

def create_matrix(N: int, S: int) -> list:
	matrix = [[randint(1, 3) for i in range(S)] for j in range(N)]

	return matrix

def divide_matrix(matrix: list, P: int) -> list:
	row_size = len(matrix[0])
	matrices_number = len(matrix) // P

	while matrices_number * P - len(matrix):
		matrix.append([0] * row_size)
		matrices_number = len(matrix) // P

	matrices = [[matrix[matrices_number * i + j] for j in range(matrices_number)] for i in range(P)]

	return matrices

def create_multimatrix(matrices: list, P: int) -> list:
	row_size = len(matrices[0][0])
	column_size = len(matrices[0])

	zero_matrix = [[0] * row_size for i in range(column_size)]

	multimatrix = [matrices[i:] + [zero_matrix] * i if i else matrices for i in range(len(matrices))]

	multimatrix_rows = [[] for i in range(column_size * len(multimatrix))] 

	for i, matrices in enumerate(multimatrix):
		for j, matrix in enumerate(matrices):
			for k, row in enumerate(matrix):
				multimatrix_rows[i * column_size + k].append(row)

	multimatrix = [[] for i in range(column_size * len(multimatrix))]
	for i, row in enumerate(multimatrix_rows):
		for subrow in row:
			multimatrix[i] += subrow

	return multimatrix

def find_critical_time(matrix: list) -> int:
	for row in matrix:
		row.append(0) 
	matrix.append([0] * len(matrix[0]))

	i = j = 0
	critical_time = matrix[i][j]
	critical_path = [[0, 0]]
	while True:
		if [matrix[i + 1][j], matrix[i][j + 1]] == [0, 0]:
			matrix.pop(-1)
			for row in matrix:
				row.pop(-1)
			return [critical_time, critical_path]
		elif not matrix[i + 1][j]:
			j += 1
			critical_path.append([i, j])
			critical_time += matrix[i][j]
			continue
		elif not matrix[i][j + 1]:
			i += 1
			critical_path.append([i, j])
			critical_time += matrix[i][j]
			continue
		right = matrix[i][j + 1]
		down = matrix[i + 1][j]

		if right < down:
			i += 1
			critical_path.append([i, j])
			critical_time += matrix[i][j]
		else:
			j += 1
			critical_path.append([i, j])
			critical_time += matrix[i][j]
			
def main():
	N = 9
	S = 4
	P = 3

	matrix = create_matrix(N, S)
	print('Initial matrix:')
	print_matrix(matrix)

	matrices = divide_matrix(matrix, P)
	print('Submatrices:')
	for submatrix in matrices:
		print_matrix(submatrix)

	multimatrix = create_multimatrix(matrices, P)
	critical_time, critical_path = find_critical_time(multimatrix)
	print('Multimatrix:')
	print_matrix_with_critical_path(multimatrix, critical_path)
	print(f'Critical time: {critical_time}')

if __name__ == '__main__':
	main()
