import requests, json
from urllib2 import urlopen
choices = ["regular", "kitty", "none"]
choices2 = ["short", "file"]
ask = " "
ask2 = " "
width = None
height = None
def sep(s, n):
  print s * n
sep(" ", 1)
sep("#", 50)
print """Type 'Regular' if You Would Like a Regular Placeholder.
Type 'Kitty' if You Would Like a Kitty Placeholder."""
while ask.lower() not in choices:
	ask = raw_input("")
sep("#", 50)
sep(" ", 1)
sep("@", 20)
while type(width) != str or type(height) != str:
	width = raw_input("Width: ")
	height = raw_input("Height: ")
	try:
		int(width)
		int(height)
	except ValueError:
		width = None
		height = None
sep("@", 20)
sep(" ", 50)
if ask.lower() == choices[0]:
	url = "http://placehold.it/%sx%s" % (width, height)
	placeholder = urlopen(url).read()
	sep("-", 50)
	print "Your URL is: %s" % url
	sep("-", 50)
	sep(" ", 1)
elif ask.lower() == choices[1]:
	url = "http://placekitten.com/%s/%s" % (width, height)
	placeholder = urlopen(url).read()
	sep("-", 50)
	print "Your URL is: %s" % url
	sep("-", 50)
	sep(" ", 1)
sep("#", 50)
print """Type 'Short' if You Would Like Your URL Shortened.
Type 'File if You Would Like Your Placeholder Written in a File Called 'placeholder.jpeg'?"""
while ask2.lower() not in choices2:
	ask2 = raw_input("")
sep("#", 50)
sep(" ", 1)
if ask2.lower() == choices2[0]:
	query_params = {'access_token': 'c86741df661ee4f3c1515ab53567ead0c58cd9ec',
	'longUrl': url}
	endpoint = "https://api-ssl.bitly.com/v3/shorten"
	response = requests.get(endpoint, params = query_params)
	data = json.loads(response.content)
	sep("-", 50)
	print "Your URL is: %s" % data['data']['url']
	sep("-", 50)
	sep(" ", 1)
elif ask2.lower() == choices2[1]:
	with open("placeholder.jpeg", "w") as myfile:
		myfile.write(placeholder)
	print """File Written.
	"""