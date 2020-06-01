import random


def ideas():
	satisfied = False

	response = [
		"Sounds shit",
		"meh",
		"Maybe.....? nah",
		"nah",
		"Are you even trying"
		]
	while not satisfied:
		input("Insert your idea: ")
		if(random.randint(0, 1000000000000000000000) == 1000000000000000000000):
			print("sounds alright, I guess...")
			satisfied = True
		else:
			print(random.choice(response))
			
if __name__ == "__main__":
	ideas()