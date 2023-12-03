_sum = 0
threes = 0
fives = 0

for i in range(1, 51):
	if i % 2 == 0:
		if i % 3 == 0:
			print("Three")
			threes += 1
		elif i % 5 == 0:
			print("Five")
			fives += 1

		_sum += i; 
	print(i)

print(f"\nSum of even numbers = {_sum}")
print(f"{threes} numbers replaced by 'Three'")
print(f"{fives} numbers replaced by 'Five'")