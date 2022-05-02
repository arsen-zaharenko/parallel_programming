from random import randint

def print_matrix(matrix: list):
	for row in matrix:
		print(' '.join(map(str,row)))
	print()

def create_matrix(N: int, S: int) -> list:
	return [[randint(1, 3) for i in range(S)] for j in range(N)]

def Bm(matrix: list, P: int, N: int, S: int, M: int, i : int) -> int:
	return sum([max([0] + [sum([matrix[(M - 1) * P + q][w] for w in range(v)]) - sum([matrix[(M - 1) * P + q + 1][w] for w in range(v - 1)]) for v in range(S)]) for q in range(i - 1)])

def Em(matrix: list, P: int, N: int, S: int, M: int, i : int) -> int:
	return Bm(matrix, P, N, S, M, i) + sum([matrix[(M - 1) * P + i - 1][w] for w in range(S)])

def Tm(matrix: list, P: int, N: int, S: int, M: int) -> int:
	return sum([max([0] + [sum([matrix[(M - 1) * P + i][j] for j in range(u)]) - sum([matrix[(M - 1) * P + i + 1][j] for j in range(u - 1)]) for u in range(S)]) for i in range(P - 1)]) + sum([matrix[(M - 1) * P + P][j] for j in range(S)])

def bm(matrix: list, P: int, N: int, S: int, M: int, i : int) -> int:
	return Bm(matrix, P, N, S, M, i) + sum([Tm(matrix, P, N, S, m) for m in range(N // P)])

def em(matrix: list, P: int, N: int, S: int, M: int, i : int) -> int:
	return Em(matrix, P, N, S, M, i) + sum([Tm(matrix, P, N, S, m) for m in range(N // P)])

def sigma_1(matrix: list, P: int, N: int, S: int, M: int) -> int:
	return min([bm(matrix, P, N, S, M + 1, i) - em(matrix, P, N, S, M, i) for i in range(P)])

def sigma_2(matrix: list, P: int, N: int, S: int, M: int) -> int:
	return min([bm(matrix, P, N, j, M + 1, 1) - em(matrix, P, N, j, M, P) for j in range(S)])

def sigma(matrix: list, P: int, N: int, S: int) -> int:
	return sum([min(sigma_1(matrix, P, N, S, m), sigma_2(matrix, P, N, S, m)) for m in range(N // P)])

def sigma_r(matrix: list, P: int, N: int, S: int, M: int, i : int) -> int:
	return sigma(matrix, N - (N // P) * P, N, S, M, i)

def T(matrix: list, P: int, N: int, S: int) -> int:
	if N <= P:
		return sum([max([sum([matrix[i][j] for j in range(u)]) - sum([matrix[i + 1][j] for j in range(u - 1)]) for u in range(S)]) for i in range(N - 1)]) + sum([matrix[N - 1][j] for j in range(S)])
	elif N % P:
		return int((sum([Tm(matrix, P, N, S, m) for m in range(N // P)]) + Tm(matrix, N - (N // P) * P, N, S, N // P) - sigma(matrix, P, N, S) - min(sigma_1(matrix, P, N, S, N // P - 1), sigma_2(matrix, P, N, S, N // P - 1))) * 0.6)

	return int((sum([Tm(matrix, P, N, S, m) for m in range(N // P)]) - sigma(matrix, P, N, S)) * 0.5)

def main():
	N = 9
	S = 4
	P = 3
	
	matrix = create_matrix(N, S)
	print('Initial matrix:')
	#print_matrix(matrix)

	print(f'Critical time: {T(matrix, P, N, S)}')

if __name__ == '__main__':
	main()