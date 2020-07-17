# This tab is mainly used to scrap data from the big 4 company.
# 1). Google inc.
# 2). FaceBook
# 3). Amazon
# 4). Apple inc. 

# Include GitHub, just for fun

# The Google data scrap
# Task: Give a user accesibilty to go anywhere, and find data; in form of HTML. In any companies
# that posseses correlation with Google; like YouTube, Gmail and etc. Good luck!
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import random

# Custom modules and libraries for the program
def googleUrl(url):
	return url

def log_error(a):
	print(a)

# The module consists of errors, attachments and many more. It also 
# includes alternative
def google_error(e):
	print(e)

def invalid_error(x):
	print(x)

def googleData():
	"""
	Includes a user-interface and then, it also includes
	Google's data in form of HTML format. Interestingly, it should also
	inlclude other companies data; with correlation with Google. 
	"""
	# The main contribution is a user-interface
	user = input("Which Google owned website would you like to visit: ")

	try:
		with closing(get(url, stream=True)) as resp:
			if closing(resp):
				return resp.content
			else:
				return None
	# When typing an incoherrent URL, it returns a "log error"; which means
	# the program has a difficulty on comprehensing the URL and it's data.
	except RequestException as a:
		log_error("Invalid website {0} and {1}" + str(a) + url)
		return None
	# When typing an URL, that is unknown to any domain. It returns an invalid 
	# error. It notifies the user that the website is unknown to any server. 
	if RequestException == x:
		invalid_error("The URL is invalid {0} and {1}" + url + str(x))


	# The statement will be a mojor aspect
	if user == "youtube" or user == "YouTube":
		googleUrl("https://www.google.com/")
		return ("You may be assisted to {0} and {1}" + resp.content("https://www.google.com/"))
	elif user == "gmail" or user == "Gmail":
		googleUrl("https://www.google.com/gmail/about/#")
		return ("you may be assisted to {0} and {1}" + googleUrl("https://www.google.com/gmail/about/#") + resp.content("https://www.google.com/gmail/about/#"))
	else:
		return None

# The Amazon URL data(Amazon Japan)

# Extra modules or libraries
def amazonUrl(i):
	i = "https://www.amazon.co.jp/b/?ie=UTF8&language=en_US&node=1094656"
	return i

def random_places(x):
	# It will take users to random places on Amazon
	aPlace = "https://www.amazon.co.uk/slp/psg-kit/72yfuorxvk3x84k"
	main = "https://www.amazon.co.jp/b/?ie=UTF8&language=en_US&node=1094656"
	x = [aPlace, main]
	# The main function code
	take = random.randint(x)
	return take

# Custom errors
def log_errors(e):
	print(e)

def invalid_item(x):
	print(x)

def access_error(z):
	print(z) # Only occurs when a request has no accessibility, but it usually does not happen. 

def search_error(i):
	print(i) # Occurs when a user; creates a typo, or when the site is non-existant.

# The most essential variable, it gives the user access
amazonUrl = "https://www.amazon.co.jp/b/?ie=UTF8&language=en_US&node=1094656"

def amazonData(url):
	# The main code; it will be the most basic section of the whole program, or at least, the most
	# similar compared to the codes written above. 
	#AmaUserItem = input("Type in an item: ") # Item search Amazon

	amazonUrl =  "https://www.amazon.co.jp/b/?ie=UTF8&language=en_US&node=1094656"

	# Trying new methods
	gamble = random.randint(0,9)
	# This statement will be major indicator, also this is just for fun.
	# The gamble function will generate a certain number, and there are alternatives for
	# any number given. The statements will include HTML results, in many different formats. It will also
	# include, "breaks", which means the program ends there. Many more!
	while 2 == 2:
		# Including major aspects
		if gamble == 1:
			result = resp.check(amazonUrl)
			return result
		elif gamble == 2:
			log_error("Your website is not validated, {0} and {1}" + url)
			return break
		elif gamble == 3:
			with gamble == 3 as amazonUrl:
				modification = resp.content(["Content-Type"].lower())
				return modification
		elif gamble == 4:
			pass
		elif gamble == 5:
			return (amazonUrl == 1 or amazonUrl is not None > 0)
		elif gamble == 6:
			search_error("Your decission you have made in your life has lead you to this statement, {1} and {0}" + resp.content("https://www.amazon.co.jp/b/?ie=UTF8&language=en_US&node=1094656"))
			True
		elif gamble == 7:
			break
		elif gamble == 8:
			# Type in the code
			pass
		else:
			True
	if url != amazonUrl:
		search_error("Webpage not found, check your URL once again, then we may assist you to your site. {0} and {1}" + str(I) + url + " is invalid")
		return None
	elif url == amazonUrl:
		return ("You may be assisted to " + resp.content( "https://www.amazon.co.jp/b/?ie=UTF8&language=en_US&node=1094656") + ", enjoy the HTML format.")
	else:
		return True
	# To engage with my inner creativity, it will not be that creative, but; who cares! XD 
	try:
		except amazonUrl as True:
			if amazonUrl == True:
				with amazonUrl:
					# It will execute the overall HTML format of Amazon
					# Only works HTTPS domain, apparently...
					result = resp.content(["Content-Type"].lower())
					# Calling the HTML format, therefore, this program maybe; further advanced
					return (result == 100 or result is not None > -1)
			else:
				# When the amazon URL is 
				result = resp.content("html.parser", url)
				amazonUrl =False
				return result