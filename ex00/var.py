def define_and_display_var():
	list = [42, "42", "quarante-deux", 42.0, True, [42], {42: 42}, (42,), set()]
	for i in list:
		print(i, "est de type", type(i))

if __name__ == '__main__':
	define_and_display_var()