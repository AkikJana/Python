import json
data=json.load(open("data.json"))

def translate(w):
	w=w.lower()
	if w in data:

		return data[w]
	else:
		return "the word does not exist."


word=input("enter word: ")
print(translate(word))  