# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

import datetime

today = datetime.date.today()


#just import a single function from module
from datetime import date

today = date.today()

print(today)

import time
timestamp = time.time()

print(timestamp)

from time import time
timestamp = time()

print(timestamp)

#Pip Modules
from camelcase import CamelCase

c = CamelCase()
print(c.hump('hello there world'))