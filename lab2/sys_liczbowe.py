def convert_to_16(number):
    	return hex(number)

def convert_to_binary(number):
	return bin(number)


def get_num():
	while True:
		try:
			number = int(input("Wprowadz liczbe w systemie 10: "))
			return number
		except ValueError:
			print("Wprowadz liczbe!")

def menu(choice):
	number = get_num()
	while(choice != "q"):
		print(
		"""Menu
		Wprowadz odpowiedni znak aby wybrac opcje
		1 - wprowadź nową liczbę w systemie 10
		2 - konwertuj do systemu dwojkowego
		3 - konwertuj do systemu 16
		q - wyjdź z programu
		""")

		choice = input()
		if choice == "1":
			number = get_num()

		elif choice == "2":
			print("Twoja liczba w systemie binarnym to: ")
			print(convert_to_binary(number))
	
		elif choice == "3":
			print("Twoja liczba w systemie 16 to: ")
			print(convert_to_16(number))
	
		elif choice == "q":
			print("Do zobaczenia!")
		else:
			print("Wybrana opcja jest niepoprawna.")

choice = ""
menu(choice)