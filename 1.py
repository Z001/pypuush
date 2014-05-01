import random
import string
import urllib
from urllib import urlopen

counter1 = 0
download = int(raw_input("How many attempts you like to try?: "))
char_set = string.digits
char_set1 = string.ascii_lowercase
char_set2 = string.ascii_uppercase
char_set3 = string.ascii_uppercase + string.digits

for i in range(download):
	rand = ''.join(random.sample(char_set*1, 1)) + ''.join(random.sample(char_set1*1, 1)) + ''.join(random.sample(char_set2*1, 1)) + ''.join(random.sample(char_set1*1, 1)) + ''.join(random.sample(char_set3*1, 1)) + '.png'
	fname = 'http://puu.sh/' + rand 
	content = urlopen('http://puu.sh/' + rand).read()
	length = len(content)
	if length > 100:
		fo = open("{0}".format(rand), "wb")
		fo.write(content);
		fo.close()
		print fname , 'downloaded' , length, "bytes"