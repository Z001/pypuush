# -*- coding: utf-8 -*-
import random
import string
import urllib
from urllib import urlopen



download = int(raw_input("How many attempts you like to try?: "))
counter1 = 0
char_set = string.digits
char_set1 = string.ascii_lowercase
char_set2 = string.ascii_uppercase
char_set3 = string.ascii_uppercase + string.digits


while counter1 <= download:
	rand = ''.join(random.sample(char_set*1, 1)) + ''.join(random.sample(char_set1*1, 1)) + ''.join(random.sample(char_set2*1, 1)) + ''.join(random.sample(char_set1*1, 1)) + ''.join(random.sample(char_set3*1, 1)) + '.png'
	fname = 'http://puu.sh/' + rand
	rcode = urlopen('http://puu.sh/' + rand).getcode()
	if rcode == 200:
		content = urlopen('http://puu.sh/' + rand).read()
		length = len(content)
		fo = open("{0}".format(rand), "wb")
		fo.write(content);
		fo.close()
		counter1 += 1
		print fname , rcode, 'downloaded' , length, "bytes"
	elif rcode == 300:
		print "Отсоси у программиста"
