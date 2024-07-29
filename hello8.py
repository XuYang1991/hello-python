import glob
from datetime import datetime
glob.glob('*.py')
test_flag = True
if test_flag:
    print("test_flag is True")
    print("test_flag is True2222")
def my_print(var):
    print(var + " is printed")

my_print("hello")
now = datetime.now()
print(now)
print(repr(1 / 10))
print (0.1 + 0.1 + 0.1 == 0.3)

from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        #if line.startswith('datetime'):
        print(line.rstrip())

