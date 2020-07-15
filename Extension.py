from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def log_error(e):
	print(e)

def boolean_eror(n)
	n = f"Error, invalid webpage"
	return n

def content(format):
	# Type in the code...
	pass

def htmlContent(content):
	# Type in the code...
	pass

	
def getUrl(url):
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

# It will execute the HTML format
print(getUrl("https://www.google.com/"))
