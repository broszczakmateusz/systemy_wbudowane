from machine import Pin
import time

morse_code = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
	'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 
	'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
	'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--',
	'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--',
	'4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
	'0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-',
	'(':'-.--.', ')':'-.--.-', '!':'-.-.--', ' ': ' '} 
	
def led_dot():
	led.off()
	time.sleep(0.5)
	led.on()
	time.sleep(0.5)

def led_dash():
	led.off()
	time.sleep(1.5)
	led.on()
	time.sleep(0.5)

def led_pause(): #odstep pomiedzy znakami/literami 
	#w sumie trwa 1.5s - 3 kropki
	time.sleep(1)

def led_space(): #odstep pomiedzy słowami 
	#w sumie trwa 3.5s - 7kropek
	time.sleep(2)

def led_morse(word):
	for w in word:
		if w ==' ':
			led_space()
		else:
			try :
				code = morse_code[w]
				for c in code:
					if c == ".":
						led_dot()
					elif c == "-":
						led_dash()
			except KeyError :
				print ("Wprowadzony znak nie jest obsługiwany!")

led = Pin(2, Pin.OUT)
led.on()

choice = ""
while (choice != "q"):
	choice = input("""Menu:
		Wprowadz odpowiedni znak aby wybrac opcje:
		p - Wprowadź nowe słowo
		q - Wyjdź z programu
		""")

	if choice == "p":
		
		try :
			word = input("Podaj słowo do zakodowania: ")
			word = word.upper()

		except ValueError :
			print ("Wprowadź słowo!")

		code = ""
		try :
			for w in word:
				code += morse_code[w]

			print("Twoje słowo w kodzie Morse'a: " + code)
			time.sleep(2)
			led_morse(word)
			

		except KeyError :
			print ("Wprowadzony znak nie jest obsługiwany!")
			
	elif choice == "q":
		print("Do zobaczenia!")

	else:
		print("Błąd wyboru opcji")
