def read_and_display_numbers():
	with open("numbers.txt", "r") as f:
		text = f.read()
		for i in text.split(","):
			print(i)


if __name__ == '__main__':
	read_and_display_numbers()