print("Importing random")
import random as rd
print("REXP has lunched succesfully")
print('''	  mmmmm  mmmmmm m    m mmmmm 
	  #   "# #       #  #  #   "#
	  #mmmm" #mmmmm   ##   #mmm#"
	  #   "m #       m""m  #
	  #    " #mmmmm m"  "m # Fixed''')

print("CREDITS: 1")
print("START: 2")
print("SRC: 3")
user = int(input("ENTER A NUMBER: "))
stop = False

if user == 1:
	print("Brosip :*)")
elif user == 2:
	print("starting REXP")
	def REXP():
		userN = int(input("How many Codes?"))
		import random
		import string

		def generate_random_string(length=10):
			chars = string.ascii_uppercase + string.digits
			return ''.join(random.choices(chars, k=length))

		# Generate 5 random strings
		random_strings = [generate_random_string() for _ in range(userN)]
		print(random_strings)

	REXP()
