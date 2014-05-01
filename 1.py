import random
import string
import urllib
counter1 = 0
char_set = string.ascii_uppercase + string.digits + string.ascii_lowercase
while counter1 <=200:
	a = ''.join(random.sample(char_set*5, 5))
	b = 'http://puu.sh/' + a + '.jpg'
	counter1 += 1
	print b
	urllib.urlretrieve(b, a + '.jpg')

	
		
		


	
