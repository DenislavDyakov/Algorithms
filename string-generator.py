characters = "emosawe si Thsi."
document = "This is awesome."

#Generate a fuction that takes a string with mixed letters and check if can generate a document with the ordered letters.

def generate_document(characters, document):
	dict = {}
	
	for char in characters:
		if char not in dict:
			dict[char] = 1
		else:
			dict[char] += 1
			
	for char in document:
		if char not in dict or dict[char] == 0:
			return False
		else:
			dict[char] -= 1
			
	return True

print(generate_document(characters, document))
