#This program is meant to simulate a conversation between the user and a chat bot.

def main():
#Code
	print("Hello, my name is Jacob! What is your name?")
	userName = input("What is your name?")
	print("")

#User
	print("Hello, Jacob! My name is " + userName + ".")
	print("")

#Code
	print("Nice to meet you, " + userName + "! I can see that your name has " + userName[2:3] + " as the 3rd letter.")
	print("Can you think of an object that starts with " + userName[2:3] + "?")
	print("")

	object = input("What's an object that starts with " + userName[2:3] + "?")

	if(userName[2:3] == "a"):
		print("Hmmm.... How about an " + object + "?")
	
	elif(userName[2:3] == "e"):
		print("Hmmm.... How about an " + object + "?")
	
	elif(userName[2:3] == "i"):
		print("Hmmm.... How about an " + object + "?")
	
	elif(userName[2:3] == "o"):
		print("Hmmm.... How about an " + object + "?")

	else:
		print("Hmmm.... How about a " + object + "?")

#Code
	print("")
	print("I love " + object + "!")
	print("But do you know what I love more?")
	print('"Big Iron".')
	print("")

#This to next comment is not required

	print("To the town of Agua Fria rode a stranger one fine day")
	print("Hardly spoke to folks around him didn't have too much to say")
	print("No one dared to ask his business no one dared to make a slip")
	print("For the stranger there among them had a big iron on his hip")
	print("Big iron on his hip")
	print("")
	print("It was early in the morning when he rode into the town")
	print("He came riding from the south side slowly lookin' all around")
	print("He's an outlaw loose and running came the whisper from each lip")
	print("And he's here to do some business with the big iron on his hip")
	print("Big iron on his hip")
	print("")
	print("In this town there lived an outlaw by the name of Texas Red")
	print("Many men had tried to take him and that many men were dead")
	print("He was vicious and a killer though a youth of twenty four")
	print("And the notches on his pistol numbered one and nineteen more")
	print("One and nineteen more")
	print("")
	print("Now the stranger started talking made it plain to folks around")
	print("Was an Arizona ranger wouldn't be too long in town")
	print("He came here to take an outlaw back alive or maybe dead")
	print("And he said it didn't matter he was after Texas Red")
	print("After Texas Red")
	print("")
	print("Wasn't long before the story was relayed to Texas Red")
	print("But the outlaw didn't worry men that tried before were dead")
	print("Twenty men had tried to take him twenty men had made a slip")
	print("Twenty one would be the ranger with the big iron on his hip")
	print("Big iron on his hip")
	print("")
	print("The morning passed so quickly it was time for them to meet")
	print("It was twenty past eleven when they walked out in the street")
	print("Folks were watching from the windows every-body held their breath")
	print("They knew this handsome ranger was about to meet his death")
	print("About to meet his death")
	print("")
	print("There was forty feet between them when they stopped to make their play")
	print("And the swiftness of the ranger is still talked about today")
	print("Texas Red had not cleared leather fore a bullet fairly ripped")
	print("And the ranger's aim was deadly with the big iron on his hip")
	print("Big iron on his hip")
	print("")
	print("It was over in a moment and the folks had gathered round")
	print("There before them lay the body of the outlaw on the ground")
	print("Oh he might have went on living but he made one fatal slip")
	print("When he tried to match the ranger with the big iron on his hip")
	print("Big iron on his hip")
	print("")
	print("Big iron Big iron")
	print("")
	print("When he tried to match the ranger with the big iron on his hip")
	print("")
	print("Big iron on his hip")

#This to previous comment is not required

#Code
	print("")
	print("")
	print("So? What do you think?")

#User
	print("")
	
	feeling = input("How do you feel about 'Big Iron' (It's a song)")
	
	if(feeling[0:1] == "I"):
		if(feeling[7:9] == "it"):
			print(feeling)
		elif(feeling[10:12] == "it"):
			print(feeling)
		elif(feeling[7:16] == "Big Iron"):
			print(feeling)
		elif(feeling[10:18] == "Big Iron"):
			print(feeling)
		else:
			print(feeling + ' "Big Iron".')
	elif(feeling[5:7] == "it"):
		print("I " + feeling)
	elif(feeling[8:10] == "it"):
		print("I " + feeling)
	elif(feeling[5:14] == "Big Iron"):
		print("I " + feeling)
	elif(feeling[8:17] == "Big Iron"):
		print("I " + feeling)
	else:
		print("I " + feeling + ' "Big Iron".')
main()
