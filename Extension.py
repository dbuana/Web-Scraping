# Challenge 2; Create a sports prediction algorithm
# Content of the code: The date of match, user may choose any team sport, the random function, on matchday the programs score will be checked
import time
import random

def sportsCategory():
	# Rule
	print("The sport must be a team sport; with a famous reputation")
	# Rule

	# The important interface
	sportsChoice = input("Choose a sport: ")

	if sportsChoice == "Football" or sportsChoice == "Soccer":
		print("Your option is valid")
	elif sportsChoice == "Basketball":
		print("Your option is valid")
	elif sportsChoice == "American Football":
		print("Your option is valid")
	else:
		print("Your choice was not valid")
	return sportsChoice

# Creating the prediction algorithm, it will only consist of sports mentioned
# Basketball, Football,  American Football and I will add more; for future references
# The algorithm will include many statements and "while loops"
import urllib.request

def predictionFootball(sportsCategory):
	userTeam = input("What team do you support: ")
	opposingTeam = input("Type in the opposing team: ")
	# Match data
	teamDate = int(input("Type in the match date: "))
	teamMonth = int(input("Type in the match month: "))
	teamLocation = input("Type in the location of the match: ")
	# Not going to include year, because that is an obvious information. No advance program needed.

	# "While loop" will be a major contributor on this program
	# This should be filled one week prior to the match
	while userTeam == True:
		print("Retrieving data from the team...")
		for x in rangen(3):
			print("Loading...")

		if userTeam == True:
			dataCompiled = f"{teamDate}/{teamMonth}/2020. Football team {userTeam} is playing against {opposingTeam}"
			scoreCompiled = f"{userTeam} {random.randint(0,9)} - {opposingTeam} {random.randint(0,9)}"

		# Where the time module has the advantage
		sleep.time(NUM)
		if time.sleep == 2081616:
			# Football matches usually happen in week, therefore, after one week; it collects data from a source to get the match points
			with urllib.request.urlopen("search?sxsrf=ALeKk01dJT_BD-FrfgL6AOfB2-jVuYxq2g%3A1594698167073&ei=tykNX6CBBJXv-QbK-YZw&q=uefa+champions+league+next+match&oq=uefa+champions+league+next+&gs_lcp=CgZwc3ktYWIQARgAMgIIADICCAAyAggAMgIIADICCAA6BAgAEEc6BAgjECc6BAgAEENQ2RlY_jZg_kBoAHABeACAAecBiAGcB5IBBTIuNC4xmAEAoAEBqgEHZ3dzLXdpeg&sclient") as response:
				html = response.read()

			matchScore = urllib.request.Request("search?sxsrf=ALeKk01dJT_BD-FrfgL6AOfB2-jVuYxq2g%3A1594698167073&ei=tykNX6CBBJXv-QbK-YZw&q=uefa+champions+league+next+match&oq=uefa+champions+league+next+&gs_lcp=CgZwc3ktYWIQARgAMgIIADICCAAyAggAMgIIADICCAA6BAgAEEc6BAgjECc6BAgAEENQ2RlY_jZg_kBoAHABeACAAecBiAGcB5IBBTIuNC4xmAEAoAEBqgEHZ3dzLXdpeg&sclient")
			# The "urllib.request" helps retrieve data from a website. Then it will display the score in the program
			# Basucally, web scraping is a major contributor to the prediction method
			result = f"{userTeam}{matchScore} - {matchScore}{userTeam}"
		return result

# Since UCL will be hosted soon, creating this function would be ideal for football fans or "betting events"; for predicting match scores
# When each round is finished another program will be created
import random
import urllib.request

def UCLprediction(sportsCategory):
	# A brief information on the UCL matches
	print("Round 16; 2 leg of the UCL matches")
	print("")
	print("a) Juventus vs Olympique Lyon")
	print("b) Paris Saint-Germain vs Atalanta")
	print("c) Manchester City vs Real Madrid")
	print("d) Chelsea vs Bayern Munich")
	print("e) Barcelona vs Napoli")

	# A user may choose the match depending on the letters
	uclTeam = input("Type in the letter of the UCL match you wish to predict: ")

	# For leissure purposes
	for x in range(5):
		print("Loading...")

	if uclTeam == True:
		predictionResult = f"{uclTeam}{random.randint(0,9)} - {random.randint(0,9)}{uclTeam}"
	else:
		None

	anotherPrediction = input("Would you like to generate another prediction for another team(Type in yes): ")
	# Another prediction for another team
	while anotherPrediction == "yes" or anotherPrediction == "y":
		amount = 1 # Expected prediction amount
		if anotherPrediction == True:
			pass
		elif anotherPrediction == False:
			break

		for x in anotherPrediction:
			if anotherPrediction != amount:
				amount += 1
			elif anotherPrediction == amount:
				predictionResult = f"{uclTeam}{random.randint(0,9)} - {random.randint(0,9)}{uclTeam}"
				return predictionResul
			else:
				None
		# Using a boolean to seek the potential within

	# The usage of the "time module" could be more sophisticated
	time.sleep(NUM)
	# Wait until August 8, 2020; the matches will occur
	# It will be assisted by "while loop" and the dunction should execute perfectly
	while time.sleep == 2081616 and uclTeam == True:
		# Type in the code... Make it as sophisticated as possible
		userOffer = input("Would you like to see the result: ")
		if userOffer == "yes" or userOffer == "Yes" or userOffer == "y" or userOffer == "Y":
			print("You may have access")
			pass
		else:
			break
		# Where the data scrapping progress happends
		with urllib.request.urlopen("") as response:
			html = response.read

		matchResults = request.Request.urlopen("") # Where the data/web scraping occurs; however, it will be enhanced by tonight
		# Found a more sophisticated, maybe not as efficient, but more sophisticated code and it runs swell!

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def log_error(e):
	print(e)

def UCLdata(url):
	# A rought draft of the code...
	try:
		with closing(get(url, stream=True)) as resp:
			if closing(resp):
				return resp.content
			else:
				return None

	except RequestException as e:
		log_error("An error occured {0} and {1}" + str(e) + url)
		return None

	if resp.content() == True:
		result = resp.content(["Content-Type"].lower())
		return (result == 100 is not None)
	else:
		return None

print(UCLdata("Google.com"))


#def nextRoundPrediction(sportsCategory):
	# Type in the code...
