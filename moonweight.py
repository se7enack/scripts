#!/usr/bin/env python3

def moon(x):
	nWeight=float(x)
	nMoonWeight=nWeight*0.165
	print("Your weight on the moon would be", nMoonWeight, "pounds.")

sWeight=input("What is your weight? \n")
try:
	val = int(sWeight)
except ValueError:
	try:
		val = float(sWeight)
	except ValueError:
		print(sWeight, "is not a number. Try again.")
		exit()

moon(sWeight)
