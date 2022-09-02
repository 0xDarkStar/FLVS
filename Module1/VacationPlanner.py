'''
Meant to calculate cost of: 
	A vacation for two days and one night
	User's (restricted) preference of foods
	Attractions, tours, and/or rides the user might go on
'''

import time
import math

def main():

	print("\n\nYou're planning on taking a vacation that'll last two days and one night to cool down after working for your tiring job for years.\n")
	time.sleep(3)
	startRegion = input("What region are you in? North America, Central America, South America, Europe, Middle East, Aisa, Oceana, or Africa? \n(Please, no caps, it won't work if you put caps) ")
	startRegion_length = len(startRegion)
	print("") #I couldn't find a way to do this without messing something else up...

	dots = [".", ".", "."]
	a = 0
	b = 0

	while(startRegion_length == 0):
		while(a <= 2):
			print("" + dots[a], end ="", flush = True)
			time.sleep(1.25)
			a += 1
		print("\n\nYou didn't input a region")
		time.sleep(1)
		startRegion = input("What region are you in? North America, Central America, South America, Europe, Middle East, Aisa, Oceana, or Africa? \n(Again, no caps, it won't work if you put caps) ")
		startRegion_length = len(startRegion)
		b += 1
		if(b == 3):
			print("You know what, since you aren't taking me seriously, fuck you!")
			quit()

	if 'north' in startRegion:
		startCountry = input("\nWhich country are you in? Canada or U.S.A.? \n(Again, no caps...) ")

	elif 'central' in startRegion:
		startCountry = input("\nWhich country are you in? Mexico, Guatemala, Honduras, El Savador, Nicaragua, Costa Rica, or Panama? \n(Again, no caps...) ")

	elif 'south' in startRegion:
		startCountry = input("\nWhich country are you in? Colombia, Venezuela, Guyana, Surname, French Guiana, Brazil, Ecuador, Peru, Bolivia, Paraguay, Uruguay, Argentina, or Chile? \n(Again, no caps...) ")

	elif 'europe' in startRegion:
		startCountry = input("\nWhich country are you in? U.K., Ireland,")

	elif 'middle' in startRegion:
		startCountry = input("\nWhich country are you in? ")

	elif 'asia' in startRegion:
		startCountry = input("\nWhich country are you in? ")

	elif 'oceana' in startRegion:
		startCountry = input("\nWhich country are you in? ")

	elif 'africa' in startRegion:
		startCountry = input("\nWhich country are you in? ")

	else:
		print("How are you nowhere on Earth?")
		time.sleep(2)
		print("Are you an alien!?")
		time.sleep(1)
		print("Aliens aren't allowed to use this program!")
		time.sleep(1)
		quit()
main()
