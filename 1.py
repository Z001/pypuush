import random
import string
import urllib

counter1 = 0
char_set = string.digits
char_set1 = string.ascii_lowercase
char_set2 = string.ascii_uppercase
char_set3 = string.ascii_uppercase + string.digits
while counter1 <=300:
	a = ''.join(random.sample(char_set*1, 1)) + ''.join(random.sample(char_set1*1, 1)) + ''.join(random.sample(char_set2*1, 1)) + ''.join(random.sample(char_set1*1, 1)) + ''.join(random.sample(char_set3*1, 1))
	b = 'http://puu.sh/' + a + '.png'
	counter1 += 1
	print b
	urllib.urlretrieve(b, a + '.png')