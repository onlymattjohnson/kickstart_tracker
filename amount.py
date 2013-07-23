import urllib2
from bs4 import BeautifulSoup
from time import gmtime, strftime

# This idea is inspired by code launched to track ubuntu edge funding on 
# Indie Go Go.  However, this will track the funding for a Kickstarter project
# http://movebits.net/2013/07/23/ubuntu-edge-funding-level/
# https://news.ycombinator.com/item?id=6090779

# ENTER KICKSTARTER URL TO USE HERE
url = ''

# Soupify the HTML

htmldoc = urllib2.urlopen(url).read();
soup = BeautifulSoup(htmldoc)

# go through and find the amount and pass it to a variable

for thingy in soup.find_all('data'):
    try:
        # pledged seems to be the only thing that has 'data-currency'
        tempHolder = thingy['data-currency']
        amount = thingy['value']
    except:
        pass

# Place output file name and path here
output_file = "/"

# Add amount and current time to string
# http://stackoverflow.com/questions/415511/how-to-get-current-time-in-python
# However, time is in GMT so it's 5 hours ahead of Chicago 

msg = "amount: " + str(amount) + " " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\n"

print msg 

# Append data to file
# http://stackoverflow.com/questions/4706499/how-do-you-append-to-file-in-python

with open(output_file, "a") as myfile:
    myfile.write(msg)
