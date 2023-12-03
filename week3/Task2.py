inp = input("Please enter the pattern to be printed.")
if len(inp) != 1:
	print("The length of charcter should be 1.")

elif inp.lower() in ["a", "e", "i", "o", "u"]: 
	print("Vowels are not allowed in the input")

else:
	for i in range(1,9):
		if i % 2 != 0:
			for i in range(i):
				print(inp, end="")
			print("\t")