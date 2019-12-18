#!/usr/bin/python3

import time
from datetime import datetime as dt

# Create function to check whether current system time is between 8am and 4pm, then return True or False
def working_hours():
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        return True
    else:
        return False

##  Not using default hosts file while testing
#   Default hosts file locations:
#   Windows:    C:\Windows\System32\drivers\etc\hosts
#   Linux/Mac:  /etc/hosts
hosts_path = "I:\Python\projects\web_blocker\Hosts\hosts"

## Create variables for the address to re-direct to and the list of websites to re-direct
redirect = "127.0.0.1"
websites = ['www.reddit.com', 'reddit.com', 'www.yahoo.com', 'yahoo.com']


while True:
    
    if working_hours():
        print("Working hours...")

        with open(hosts_path, 'a+') as hosts:
            for site in websites:
                if (redirect + " " + site) not in hosts.read():
                    print("Adding '%s' to hosts file..." % site)
                    hosts.write("\n" + redirect + " " + site)
                    hosts.seek(0)
                else:
                    print("'%s' already added..." % site)

    else:
        print("No more work!")


    
    time.sleep(5)