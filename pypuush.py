import random
import string
import urllib
from urllib import urlopen
import datetime
import time

download = int(raw_input("How many attempts you like to try?: "))
counter1 = 0
char_set = string.digits
char_set1 = string.ascii_lowercase
char_set2 = string.ascii_uppercase
char_set3 = string.ascii_uppercase + string.digits

while counter1 < download:
	urllib.URLopener.version = 'Mozilla/5.0 (compatible; Googlebot-Image/1.01; +http://www.google.com/bot.html)'
	rand = ''.join(random.sample(char_set*1, 1)) + ''.join(random.sample(char_set1*1, 1)) + ''.join(random.sample(char_set2*1, 1)) + ''.join(random.sample(char_set1*1, 1)) + ''.join(random.sample(char_set3*1, 1)) + '.png'
	fname = 'http://puu.sh/' + rand
	rcode = urlopen('http://puu.sh/' + rand).getcode()
	t1 = time.time()
	st = datetime.datetime.fromtimestamp(t1).strftime('%Y-%m-%d %H:%M:%S')
	if rcode == 200:
		content = urlopen('http://puu.sh/' + rand).read()
		length = len(content)
		fo = open("{0}".format(rand), "wb")
		fo.write(content);
		fo.close()
		counter1 += 1

		print st, " |", fname, " |", rcode, "Ok |", 'Downloaded:' , length, "bytes."
	elif rcode == 403:
		print st, " |", fname, " |", rcode, "Forbidden |"
	elif rcode == 404:
		print st, " |", fname, " |", rcode, "Not found |"
	elif rcode == 300:
		print "Otsosi u traktorista"