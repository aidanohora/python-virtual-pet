import msvcrt #This module is the reason this program only works on windows, for unix equivalent: https://stackoverflow.com/questions/3523174/raw-input-in-python-without-pressing-enter
import time
import _thread #for multithreading
from os import system
from sys import exit

debug_mode = False

time_interval = 1 #the higher the value, the more slowly the status bars decrease

#functionality for virtual pet

class Digital: #class for the pet
	
	hunger = 100
	
	tiredness = 100
	
	health = 100
	
	asleep = False
	
	starving = False
	
	eating = False
	
	def __init__(self, name):
		self.name = name

#two threads will be run, one of which will alternate between the wake and sleep cycles below

def wake_cycle(pet):
	while pet.asleep == False and pet.health > 0:
		time.sleep(time_interval)
		if pet.hunger > 0:
			pet.hunger -= 2
		pet.tiredness -= 0.5
		if pet.hunger <= 0:
			pet.starving = True
			pet.health -= 0.5
		else:
			pet.starving = False
			if pet.hunger > 50 and pet.health < 100: #heal when awake and above half hunger
				pet.health += 0.25
		if pet.tiredness <= 0: #shouldn't drop below zero but just in case
			pet.asleep = True
	#once pet is no longer awake, a new thread is created to run the sleep cycle and this thread terminates
	_thread.start_new_thread(sleep_cycle, (pet,))
	
def sleep_cycle(pet):
	while pet.asleep == True and pet.health > 0: 
		time.sleep(time_interval)
		pet.tiredness += 1
		if pet.hunger <= 0:
			pet.starving = True
			pet.health -= 0.25
		else:
			pet.starving = False
			pet.hunger -= 1
			pet.health += 0.5
		if pet.tiredness > 100:
			pet.tiredness = 100
		if pet.tiredness == 100:
			pet.asleep = False
	#once pet is no longer asleep, a new thread is created to run the wake cycle and this thread terminates
	_thread.start_new_thread(wake_cycle, (pet,))
	
	
#functions for pet status bars, to be called in the display function	
	
def print_hunger_bar(pet):
	bar = ("[")
	y = 0
	while y < 100:
		if y < pet.hunger:
			bar = bar + "|"
		else:
			bar = bar + " "
		y = y + 10
	bar = bar + "]"
	print(" Hunger:", bar)

def print_tiredness_bar(pet):
	bar = ("[")
	y = 0
	while y < 100:
		if y < pet.tiredness:
			bar = bar + "|"
		else:
			bar = bar + " "
		y = y + 10
	bar = bar + "]"
	print(" Sleep: ",bar)

		
def print_health_bar(pet):
	bar = ("[")
	y = 0
	while y < 100:
		if y < pet.health:
			bar = bar + "|"
		else:
			bar = bar + " "
		y = y + 10
	bar = bar + "]"
	print(" Health:",bar)


#the second thread will consist of running the display function below
def display(pet):
	position = 0 #represents where the pet is on the screen
	facing_forward = True
	while pet.health > 0:
		if pet.asleep == False and pet.starving == False and pet.eating == False:
			if position == 0 and facing_forward == True:
				system("cls")
				print("""
 ________
|  o _ o |
|________|   		
						
						""")
				print(" Name:", pet.name)
				print()
				print_hunger_bar(pet)
				print()
				print_tiredness_bar(pet)
				print()
				print_health_bar(pet)
				time.sleep(1)
				position = position + 1
			elif position == 1 and facing_forward == True:
				system("cls")
				print("""
	 ________
	|  o _ o |
	|________|   		
						
						""")
				print(" Name:", pet.name)
				print()
				print_hunger_bar(pet)
				print()
				print_tiredness_bar(pet)
				print()
				print_health_bar(pet)
				time.sleep(1)
				position = position + 1
			elif position == 2 and facing_forward == True:
				system("cls")
				print("""
		 ________
		|  o _ o |
		|________|   		
						
						""")
				print(" Name:", pet.name)
				print()
				print_hunger_bar(pet)
				print()
				print_tiredness_bar(pet)
				print()
				print_health_bar(pet)
				time.sleep(1)
				position = position + 1
			elif position == 3 and facing_forward == True:
				system("cls")
				print("""
			 ________
			|  o _ o |
			|________|   		
						
						""")
				print(" Name:", pet.name)
				print()
				print_hunger_bar(pet)
				print()
				print_tiredness_bar(pet)
				print()
				print_health_bar(pet)
				time.sleep(1)
				facing_forward = False
			elif position == 3 and facing_forward == False:
				system("cls")
				print("""
			 ________
			| o _ o  |
			|________|    		
						
						""")
				print(" Name:", pet.name)
				print()
				print_hunger_bar(pet)
				print()
				print_tiredness_bar(pet)
				print()
				print_health_bar(pet)
				time.sleep(1)
				position = position -1
			elif position == 2 and facing_forward == False:
				system("cls")
				print("""
		 ________
		| o _ o  |
		|________|    		
						
						""")
				print(" Name:", pet.name)
				print()
				print_hunger_bar(pet)
				print()
				print_tiredness_bar(pet)
				print()
				print_health_bar(pet)
				time.sleep(1)
				position = position -1
			elif position == 1 and facing_forward == False:
				system("cls")
				print("""
	 ________
	| o _ o  |
	|________|    		
						
						""")
				print(" Name:", pet.name)
				print()
				print_hunger_bar(pet)
				print()
				print_tiredness_bar(pet)
				print()
				print_health_bar(pet)
				time.sleep(1)
				position = position -1
			else:
				system("cls")
				print("""
 ________
| o _ o  |
|________|    		
						
						""")
				print(" Name:", pet.name)
				print()
				print_hunger_bar(pet)
				print()
				print_tiredness_bar(pet)
				print()
				print_health_bar(pet)
				time.sleep(1)
				facing_forward = True
		elif pet.eating == True:
			if (position != 0 and facing_forward == True) or (position != 3 and facing_forward == False):
				if facing_forward == True:
					position = position - 1 #keep pet in place while eating
				else:
					position = position + 1
			system("cls")
			if position == 0:
				print("""	   
 ________ 
|  ^__^  |
|________|   		
					
					""")
			elif position == 1:
				print("""	   
	 ________ 
	|  ^__^  |
	|________|   		
					
					""")
			elif position == 2:
				print("""	   
		 ________ 
		|  ^__^  |
		|________|   		
					
					""")
			else:
				print("""	   
			 ________ 
			|  ^__^  |
			|________|   		
					
					""")
			print(" Name:", pet.name)
			print()
			print_hunger_bar(pet)
			print()
			print_tiredness_bar(pet)
			print()
			print_health_bar(pet)
			time.sleep(1)
		elif pet.asleep == True:
			system("cls")
			print("""
	 ________ zZ
	|  - _ - |
	|________|   		
					
					""")
			print(" Name:", pet.name)
			print()
			print_hunger_bar(pet)
			print()
			print_tiredness_bar(pet)
			print()
			print_health_bar(pet)
			time.sleep(1)
		elif pet.starving == True:
			system("cls")
			print("""	   ! ! !
	 ________ 
	|  o _ o |
	|________|   		
					
					""")
			print(" Name:", pet.name)
			print()
			print_hunger_bar(pet)
			print()
			print_tiredness_bar(pet)
			print()
			print_health_bar(pet)
			time.sleep(0.5)
			system("cls")
			print("""	   ! ! !	    
	 ________ 
	|  > _ < |
	|________|   		
					
					""")
			print(" Name:", pet.name)
			print()
			print_hunger_bar(pet)
			print()
			print_tiredness_bar(pet)
			print()
			print_health_bar(pet)
			time.sleep(0.5)
	
	
	system("cls")	
	print("""
	 ________ 
	|  X _ X |
	|________|   		
						
					""")
	print(" Name:", pet.name)
	print()
	print_health_bar(pet)
			
#loading bar animation
def print_loading_bar():
	x = 1
	while x < 60:
		y = 1
		loading_bar = ("[|")
		while y < 60:
			if y < x:
				loading_bar = loading_bar + "|"
			else:
				loading_bar = loading_bar + " "
			y = y + 1
		loading_bar = loading_bar + "]"
		print()
		print("""Commands:
-"F" key to feed
-"S" key to put to sleep/wake-up
-"Q" key to quit
		""")
		print()
		print("Loading")
		print()	
		print(loading_bar)
		time.sleep(0.05)
		system("cls")
		x = x + 1			
	
#first output printed to terminal
chosen_name = input("Please enter a name for pet: ")
 
pet = Digital(chosen_name)

time.sleep(1.5)

system("cls")

if debug_mode == False:		
	print_loading_bar()

#virual pet is ran 
_thread.start_new_thread(wake_cycle, (pet,))
		

_thread.start_new_thread(display, (pet,))

#keybindings
while pet.health > 0:
	command = msvcrt.getwch()
	command = command.lower()
	if command == "f":
		if pet.asleep == True:
			pet.asleep = False
		pet.hunger += 50
		if pet.hunger > 100:
			pet.hunger = 100
		pet.eating = True
		time.sleep(1)
		pet.eating = False
	if command == "s":
		if pet.asleep == True:
			pet.asleep = False
		else:
			pet.asleep = True
	if command == "q":
		exit()
	