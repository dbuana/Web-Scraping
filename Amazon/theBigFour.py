amazonUrl = "https://www.amazon.co.jp/b/?ie=UTF8&language=en_US&node=1094656"

def amazonData(url):
	# The main code; it will be the most basic section of the whole program, or at least, the most
	# similar compared to the codes written above. 
	#AmaUserItem = input("Type in an item: ") # Item search Amazon

	amazonUrl =  "https://www.amazon.co.jp/b/?ie=UTF8&language=en_US&node=1094656"

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
