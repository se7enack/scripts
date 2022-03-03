#!/usr/bin/env python3

def moon(x):
	nWeight=float(x)
	nMoonWeightLong=nWeight*0.165
	nMoonWeight = "{:.2f}".format(nMoonWeightLong)
	print("\nYour weight on the moon would be", nMoonWeight, "pounds.\n")

sWeight=input("What is your weight? \n")
try:
	val = int(sWeight)
except ValueError:
	try:
		val = float(sWeight)
	except ValueError:
		print("\nError:",sWeight, "is not a number. Try again.\n")
		exit()

moon(sWeight)
