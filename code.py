from record import recording
import random


class Weapon:
	name = None
	price = None

	@staticmethod
	def get_weapon(x):
		if x == 0:
			return Build_Weapon("knife",random.randrange(20,30))
		if x == 1:
			return Build_Weapon("Gun",random.randrange(999,4000))

@recording
def Build_Weapon(name="Dummy",price="Free"):
	print("Building the weapon")
	return price



for _ in range(20):
	w = Weapon.get_weapon(random.randrange(2))
