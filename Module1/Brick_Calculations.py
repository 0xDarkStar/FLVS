#This program is meant to ask the user to input the dimensions of a roman brick so it can then calculate the surface area and volume
import math

def main():

	#Word problem
	print("Kevin tells the police about the brick he threw at the wet bandits.")
	print("The police want to know the dimension of the brick to find the surface area and volume of it.")
	print("All the police know is that it's a roman brick, can you help the police with the dimensions?")

	#Hehehehe, funny idea
	answer = input("Will you help the police with the dimensions of the brick? ")

	if 'y' in answer: #The User wants to help the cops
		#Variables for length, height, and width
		length = int(input("\nWhat is the length of a roman brick? "))
		print("The length of the brick is " + str(length) + " centimeters.\n")
		height = int(input("What is the height of a roman brick? "))
		print("The height of the brick is " + str(height) + " centimeters.\n")
		width = int(input("What is the width of a roman brick? "))
		print("The width of the brick is " + str(width) + " centimeters.\n")

		#Calculate surface area and volume
		surfaceArea = (length*height)*2+(length*width)*2+(width*height)*2
		volume = length*height*width
		print("The surface area of the brick is: " + str(surfaceArea))
		print("The volume of the brick is: " + str(volume))

	if 'n' in answer:	#User doesn't want to help the cops
		print("\nI guess the police would need to find another detective for the case....\n\n")
		print("MISSION FAILED")
		print("WE'LL GET 'EM NEXT TIME")

main()
