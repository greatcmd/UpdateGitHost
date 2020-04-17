s = """
github.com
assets-cdn.github.com
avatars0.githubusercontent.com
avatars1.githubusercontent.com
github-cloud.s3.amazonaws.com
documentcloud.github.com 
help.github.com
nodeload.github.com
raw.github.com
status.github.com
training.github.com
github.io
"""

#check required moudles.
import pip

def install(package):
    pip.main(['install', package])

#install('requests')
#install('BeautifulSoup')
#install('pywin32')
import sys
import subprocess
import pkg_resources


required = {'requests', 'BeautifulSoup', 'pywin32'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    for pkg in missing:
        install(pkg)


#check admin
import admin
if not admin.isUserAdmin():
        admin.runAsAdmin()


# function code    
import requests
from bs4 import BeautifulSoup
import os
  
ans = []
for i in s.split():
    url = "http://ip.chinaz.com/" + i.strip()
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text)
    x = soup.find(class_="IcpMain02")
    x = x.find_all("span", class_="Whwtdhalf")
    x = "%s %s" % (x[5].string.strip(), i.strip())
    print(x)
    ans.append(x)


# update hosts  
hosts = r"C:\Windows\System32\drivers\etc\hosts"
with open(hosts, "r") as f:
    content = [i for i in f.readlines() if i.startswith("#")]
    content.extend(ans)
with open(hosts, "w") as f:
    f.write("\n".join(content))
    

# flush dns
os.system('ipconfig /flushdns')
