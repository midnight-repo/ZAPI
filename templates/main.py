import re
import os
from pathlib import Path

{{IMPORTS_LIST}}

def launch_ZAP():
    os.system('zap.sh -daemon')

ZAP_API_KEY = re.search('<key>(\w+)</key>', open(f'{Path.home()}/.ZAP/config.xml').read())[1]

z = API('http://127.0.0.1:8081', ZAP_API_KEY)



