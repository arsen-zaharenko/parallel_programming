from math import sin

def factorial(n):
	if n in [0, 1]:
		return 1
	return n * factorial(n - 1)

def function(x):
	return sin(x * x)

def calculate_integral(A: int):
	A3 = A ** 3
	A4 = A * A3

	sum = A3 / 3

	A_power = A3 * A4
	k = -1

	for i in range(1, 51):
		sum += k * A_power / factorial(2 * i + 1) / (4 * i + 3)
		A_power *= A4
		k *= -1

	return sum 

def trapezoid_rule(f, A, n):
	dx = 1.0 * A / n
	sum = 0.5 * (f(0) + f(A))
    
	for i in range(1, n):
		sum += f(i * dx)

	return sum * dx

def main():
	N = 1_000_000

	for i in range(1, 11):
		c_i = calculate_integral(i)
		t_f = trapezoid_rule(function, i, N)

		print(f'A = {i}\n I = {c_i}\n T = {t_f}\n |I - T| = {abs(c_i - t_f)}', end='\n\n')

if __name__ == '__main__':
	main() 