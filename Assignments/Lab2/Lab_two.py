
import webbrowser
import random
from random import randint

sites=['https://maktoob.yahoo.com/?p=us','https://www.google.com.eg/','http://python-history.blogspot.com.eg/'];
webbrowser.open(sites[randint(0,len(sites))]);
