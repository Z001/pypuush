from Tkinter import *
import random
import string
import urllib
from urllib import urlopen
try: import tkinter
except ImportError:

    import Tkinter as tkinter
    import ttk
    import Queue as queue
else:

    from tkinter import ttk
    import queue

 


master = Tk()

w = Label(master, text="How many puushes would you like to download?")
w.pack()

separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

e = Entry(master)
e.pack()
e.focus_set()

counter1 = 1

def callback():

	global counter1
	download = int(e.get())
	char_set = string.digits
	char_set1 = string.ascii_lowercase
	char_set2 = string.ascii_uppercase
	char_set3 = string.ascii_uppercase + string.digits
	counter2 = 0
	progbar = ttk.Progressbar(master, maximum=download, length=300)
	progbar.pack()
	progbar['variable'] = counter2




	while counter1 <= download:

		print counter1
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
			counter2 += 1
			print fname , rcode, 'downloaded' , length, "bytes"
			progbar.update()
			progbar.step(1)

			    			
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

b = Button(master, text="Grab it!", width=10, command=callback)
b.pack()


mainloop()