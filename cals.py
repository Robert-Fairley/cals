#!/usr/bin/env python3

]import json

# """
# Variables
# ---------
# cals = Number of calories gained
#
# c = Calories gained from McDonalds meal
# x = Wildcard calories gained from other eating
# m = McDonald's meal type (multiple choice question)
# n = Number of meals consumed
# j = Basal Metabolic Rate (Harris-Benedict equation for m/f)
# k = Calories burned walking
# L = Weight in pounds(lbs)
# H = Height in inches
# F = Height (feet)
# I = Height (inches)
# G = Gender (male or female)
# A = Age
# T = Time spent walking (minutes)
# """


def harrisBenedictEq(gender_basis, weight, height, age):
	if gender_basis == 'male' or gender_basis == 'm':
		print("Running Harris-Benedict for males...")
		j = 66 + (6.2 * weight) + (12.7 * height) + (6.76 * age)
	else:
		print("Running Harris-Benedict for females...")
		j = 655.1 + ( 4.35 * weight) + (4.7 * height) + (4.7 * age)
	return j


def calsBurnedWalking(weight, time):
	k = 0.29 * weight * time
	return k


def getMcDonaldsCals(meal):
	# Default caloric content
	cal = 500

	with open('mcd.json') as mcd_list:
		mcd = json.load(mcd_list)

	if meal == "a":
		cal = mcd[0]["CAL"]
	elif meal == "b":
		cal = mcd[1]["CAL"]
	elif meal == "c":
		cal = mcd[2]["CAL"]
	else:
		cal = mcd[3]["CAL"]

	return int(cal)


def main():
	x = 0
	T = 5

	print("= = = = = = = = = = = = = = = = = = = = = = = = =")
	print("\n\nMCDONALDS DELIVERY MEAL CALORIE CALCULATOR 5000\n\n")
	print("        or MDMCC5000v0.0.4.5.2.1.62.x for short\n\n")
	print("= = = = = = = = = = = = = = = = = = = = = = = = =")
	print("\n\nSo let's go...\n\n")


	m = input("QUESTION 1:\nWhat kind of meal did you have?\n     a) Bacon Clubhouse Burger\n     b) Premium Grilled Chicken Clubhouse Sandwich\n     c) Premium Buttermilk Crispy Chicken Bacon Clubhouse Sandwich\n     d) McChicken\n Answer: ")
	n = int(input("QUESTION 2:\nHow many did you eat?: "))
	F = float(input("QUESTION 3:\nHow tall are you (feet)?: "))
	I = float(input("QUESTION 4:\nAnd how many inches?: "))
	L = float(input("QUESTION 5:\nHow much do you weight (pounds)?: "))
	A = int(input("QUESTION 6:\nHow old are you?: "))
	G = input("QUESTION 7:\nWhat's your gender (binary)?\n     m) Male\n     f) Female\nAnswer: ")
	H = (F * 12) + I
	c = getMcDonaldsCals(m)


	# Make the assumption that if the user is male, an average of 2500 cals is required
	# and consumed, but include the presumption that one McDonald's meal was planned to
	# help fulfill those requirements, so assume 2000 cals.
	# Make the assumption that if the user is a female, an average of 200 cals is required,
	# so assume 1500 cals.
	if G == 'm':
		x = 2000
	else:
		x = 1500

	# r/theydidthemath
	j = harrisBenedictEq(G, L, H, A)
	k = calsBurnedWalking(L, T)
	C = ((c * n + x) - (k + j))

	# OUTPUT
	# Print the results
	print("\n\n* * * * * * * * * * * * * * * * * * * * * * * * * * * *")
	print("                     YOUR RESULTS")
	print("                       - - - -")
	print("    Assuming you eat the average amount\n    for a human adult besides your McDonald's...\n")
	print("    You've accumulated %.2f calories" % round(C,2))
	print("    by eating %i McDonald's delivery meals!\n\n\n" % (n))

	return None

if __name__ == "__main__":
	main()
