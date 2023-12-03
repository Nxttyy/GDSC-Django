inp = input("Please enter the word to check: ").lower()
inp_reversed  = inp[:: -1]

if inp == inp_reversed:
	print(f"The word {inp} is a palindrome.") 

else:
	print(f"The word {inp} is not a palindrome because, \n {inp} is not equal with {inp_reversed}")