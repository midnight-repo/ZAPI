import re
import os
from pathlib import Path
from zapy.API import API


def launch_ZAP():
    os.system('gnome-terminal -- zap.sh -daemon')

def read_key_from_FS():  # Works only on linux
    return re.search('<key>(\w+)</key>', open(f'{Path.home()}/.ZAP/config.xml').read())[1]


launch_ZAP()
zap = API('http://127.0.0.1:8081', read_key_from_FS())

spider_id = zap.spider.spiderActionScan(url='< TARGET URL >',
                                        maxChildren=5,
                                        recurse=True)
