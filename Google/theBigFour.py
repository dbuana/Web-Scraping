# This tab is mainly used to scrap data from the big 4 company.
# 1). Google inc.
# 2). FaceBook
# 3). Amazon
# 4). Apple inc. 

# The Google data scrap
# Task: Give a user accesibilty to go anywhere, and find data; in form of HTML. In any companies
# that posseses correlation with Google; like YouTube, Gmail and etc. Good luck!
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

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


print(googleData())