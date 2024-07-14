textEntered  = "supreme court is the highest judicial court"
faultyKeys = "su"
no_of_matches = 0
pos = 0
no_of_operations = 0



for letter in textEntered:
	pos =0
	for faulty_letter in faultyKeys:
		pos += 1
		if letter == faulty_letter:

			print("\nmatched!")
			print(faulty_letter,pos)
			
			if pos == 1:
				print("entered1")
				no_of_operations += 1 #paste
				no_of_operations += len(faultyKeys) - 1
				print("no :",no_of_operations)

			if pos == len(faultyKeys):
				print("entered2")
				no_of_operations += 1
				no_of_operations += len(faultyKeys)
			
			elif pos>1 and pos<len(faultyKeys):

				print("entered3")
				no_of_operations += 1
				no_of_operations += len(faultyKeys) 
	

print("IDEAL RESULT:",17)
print(no_of_operations)
