#!/usr/bin/python3

#######
#   Script to block specific websites from loading within a certain time frame.
#
#   **Needs to be run in a terminal as an administrator or from a scheduled task/job or changed to .pyw and run as admin**
#
#######

import time
from datetime import datetime as dt

# Create function to check whether current system time is between 8am and 4pm, then return True or False
def working_hours():
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23):
        return True
    else:
        return False

#  Not using default hosts file while testing
#  Default hosts file locations:
#  --Windows:    C:\Windows\System32\drivers\etc\hosts
#  --Linux/Mac:  /etc/hosts
win_hosts = "C:\Windows\System32\drivers\etc\hosts"

## Create variables for the address to re-direct to and the list of websites to re-direct
redirect = "127.0.0.1"
websites = ['www.reddit.com', 'reddit.com', 'www.yahoo.com', 'yahoo.com']


# Create infinite loop for adding or removing items from hosts file, depending on time of day
while True:
    
    # If function returns True, it is within working hours
    if working_hours():
        print("Working hours...")

        # Open hosts file and read content to 'content' variable to work with
        with open(win_hosts, 'r+') as file:
            content = file.read()

            # For each site in the list of websites, check if the site is currently in the hosts file
            # If site is not in file, add line for "127.0.0.1 [site]", otherwise pass
            for site in websites:
                if not any(site in content for website in websites):
                    print("Adding '%s' to file..." % site)
                    file.write("\n" + redirect + " " + site)
                else:
                    pass

    # If function returns False for working hours
    else:
        print("No more work!")

        # Open hosts file and read content the same as above
        with open(win_hosts, 'r+') as file:

            # This time, read lines inidividually and store them into a list with one line per item in the list
            # Once the list is created, use file.seek(0) to move the cursor back to the beginning of the file
            content = file.readlines()
            file.seek(0)

            # For each item in the 'content' list, check if the item contains one of the websites we want to block
            # This will re-write the entire hosts file with only the lines that don't contain a website from our website list
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
                else:
                    print("Removing '%s' from file..." % line)
            file.truncate()

    # After all actions above, sleep for 5 seconds then check the loop again.
    # This can be changed to any value, depending on personal preference
    time.sleep(5)