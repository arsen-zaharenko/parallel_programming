from math import sqrt

def get_divisors(n: int):
	result = []

	for i in range(2, n + 1):
		if not n % i:
			result.append(i)

	return result

def create_stadium(rows: int, columns: int, portals: int):
	stadium = {
				'portals': portals,
				'sector': [['`'] * int(columns / portals) for i in range(rows)]
			}

	stadium['sector'][0][0] = '@'

	return stadium

def fill_stadium(stadium: dict):
	time = 0
	cost = 0
	sector = stadium['sector']
	portals = stadium['portals']

	for i in range(len(sector)):
		for j in range(len(sector[i])):
			if [i, j] != [0, 0]:
				sector[i][j] = '#'
				time += i + j
				cost += (len(sector) + len(sector[i]) * portals  - i - j)

	return time, cost

def print_stadium(stadium: dict):
	for row in stadium['sector']:
		print(''.join(map(str, row)))

def main():
	N = 20
	M = 10000
	divisors = get_divisors(M)
	data = []
	best_stadium = [1, 1]

	for i in divisors:
		stadium = create_stadium(rows=N, columns=M, portals=i)
		time, cost = fill_stadium(stadium)

		data.append({'time': time, 'cost': cost})

	for i in range(len(divisors) - 1):
		current = data[i]
		next = data[i + 1]
		k = (current['time'] / next['time']) - (next['cost'] / current['cost'])

		if k < best_stadium[1]:
			best_stadium[0] = i
			best_stadium[1] = k

	print(f'Optimal number of portals for stadium {N}x{M}: {best_stadium[0]}')

if __name__ == '__main__':
	main()
