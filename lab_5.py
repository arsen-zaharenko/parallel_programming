import matplotlib.pyplot as plt
from random import randint

def print_matrix(matrix: list):
	for row in matrix:
		print(' '.join(map(str,row)))
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

def draw_line_segment(point_1, point_2):
	plt.plot([point_1[0], point_2[0]],[point_1[1], point_2[1]])

def draw_tacts(process: int, begin: list, times: list):
	for i, time in enumerate(times):
		draw_line_segment([begin[0], process], [begin[0] + time, process])
		begin[0] += time
	begin[0] -= sum(times[1:])

def draw_plot(matrices: list, M: int):
	begin = [0]
	new_begin = [0]
	for i in range(M):
		for process, matrix in enumerate(matrices):
			if new_begin[0] < begin[0] + sum(matrix[i]):
				new_begin[0] = begin[0] + sum(matrix[i])
			draw_tacts(process + 1, begin, matrix[i])
		begin[0] = new_begin[0]

	plt.show()
			
def main():
	N = 9
	S = 4
	P = 3
	M = N // P if N // P * P == N else N // P + 1

	matrix = create_matrix(N, S)
	print('Initial matrix:')
	print_matrix(matrix)

	matrices = divide_matrix(matrix, P)
	print('Submatrices:')
	for submatrix in matrices:
		print_matrix(submatrix)

	draw_plot(matrices, M)

if __name__ == '__main__':
	main()