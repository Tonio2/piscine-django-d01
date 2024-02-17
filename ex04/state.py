import sys

def index_of_value(dict, value):
	for key, val in dict.items():
		if val == value:
			return key
	return None

def main():
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
 
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
 
	if len(sys.argv) != 2:
		return
	if sys.argv[1] in capital_cities.values():
		# Find the state that matches the capital city
		state = index_of_value(capital_cities, sys.argv[1])
		print(index_of_value(states, state))
	else:
		print("Unknown state")
  
if __name__ == '__main__':
	main()