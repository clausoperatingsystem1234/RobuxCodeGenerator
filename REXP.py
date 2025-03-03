print("Importing random")
import random as rd
print("REXP has lunched succesfully")
print('''	  mmmmm  mmmmmm m    m mmmmm 
	  #   "# #       #  #  #   "#
	  #mmmm" #mmmmm   ##   #mmm#"
	  #   "m #       m""m  #
	  #    " #mmmmm m"  "m # MAN FUCK EXPENSIVE SHIT''')

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
		userN = int(input('''How many times(the larger the better)
					 : '''))
		for i in range(userN):
			firstN = rd.randint(100, 999)
			secondN = rd.randint(100, 999)
			ThirdN = rd.randint(1000, 9999)
			print(f"{firstN}-{secondN}-{ThirdN}")
		res = input("Restart?Y/N:  ")
		if res == "Y" or "y":
			print("restarting")
			REXP()
		else:
			print("Shutting down... Thank you for  using REXP")
			print('BYE///')

	REXP()
