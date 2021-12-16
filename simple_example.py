import re
import os
import time
from pathlib import Path
from zapy.API import API


def launch_ZAP():
    os.system('gnome-terminal -- zap.sh -daemon')

def read_key_from_FS():  # Works only on linux
    return re.search('<key>(\w+)</key>', open(f'{Path.home()}/.ZAP/config.xml').read())[1]


#launch_ZAP()
zap = API('http://127.0.0.1:8081', read_key_from_FS())

sp = zap.spider.spiderActionScan(url='https://www.wikipedia.org',
                                        maxChildren=5,
                                        recurse=True)
print(sp)

