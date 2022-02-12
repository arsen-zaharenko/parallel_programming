from random import random, randint
from math import sqrt
from time import time
import multiprocessing
import os

def generate_data(N: int):
	data = list()

	for i in range(N):
		a = randint(-10, 10)
		while not a:
			a = randint(-10, 10)
		b = randint(-10, 10)
		c = randint(-10, 10)

		data.append([a, b, c])

	return data

def discriminant(coefficients: list):
	return coefficients[1]**2 - 4*coefficients[0]*coefficients[2]

def define_sign(n: int):
	if n > 0:
		return '+'
	elif n < 0:
		return '-'
	return '='

def find_roots(discriminant: int, coefficients: list):
	if not discriminant:
		return [-coefficients[1] / 2 / coefficients[0]]

	sqrt_D = sqrt(discriminant)
	x_1 = (-coefficients[1] + sqrt(discriminant)) / 2 / coefficients[0]
	x_2 = (-coefficients[1] - sqrt(discriminant)) / 2 / coefficients[0]
	
	return [x_1, x_2]

def find_complex_roots(discriminant: int, coefficients: list):
	sqrt_D = sqrt(abs(discriminant))
	x_1 = f'{-coefficients[1] / 2 / coefficients[0]} + {sqrt_D / 2 / coefficients[0]}i'
	x_2 = f'{-coefficients[1] / 2 / coefficients[0]} - {sqrt_D / 2 / coefficients[0]}i'

	return [x_1, x_2]

def solve_quadratic_equation(coefficients: list):
	D = discriminant(coefficients)

	if define_sign(D) in ['+', '=']:
		return find_roots(D, coefficients)
	return find_complex_roots(D, coefficients)

def main():
	data = generate_data(3000000)

	start_time = time()
	list(map(solve_quadratic_equation, data))
	print(f'Regular mode: {time() - start_time:.{4}}s')

	pool = multiprocessing.Pool(processes=os.cpu_count())

	start_time = time()
	pool.map(solve_quadratic_equation, data)
	print(f'Max mode: {time() - start_time:.{4}}s')

if __name__ == '__main__':
	main()