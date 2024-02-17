import sys

def index_of_value(dict, value):
	for key, val in dict.items():
		if val.lower() == value.lower():
			return key
	return None

def value_of_key(dict, value):
	for key, val in dict.items():
		if key.lower() == value.lower():
			return val
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
	for val in sys.argv[1].split(','):
		val = val.strip()
		is_capital = index_of_value(capital_cities, val)
		is_state = value_of_key(states, val)
		if is_capital:
			print(capital_cities[is_capital], " is the capital of ", index_of_value(states, is_capital))
		elif is_state:
			print(capital_cities[is_state], " is the capital of ", index_of_value(states, is_state))
		elif val != "":
			print(val + " is neither a capital city nor a state")
  
if __name__ == '__main__':
	main()