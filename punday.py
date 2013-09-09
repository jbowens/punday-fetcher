#!/usr/bin/python
import sys, urllib2, re, os
from subprocess import call

def main(argv):

    # If the punday folder doesn't exist, make it!
    userpath = os.path.expanduser('~/.punday')
    if not os.path.exists(userpath):
        os.mkdir(userpath)

    response = urllib2.urlopen('http://mondaypunday.com')
    html = response.read()
    m = re.search('src="(http://mondaypunday.com/([^"]+)/uploads/([A-z0-9]+).jpg)"', html)

    local_jpg_loc = userpath + '/' + m.group(3) + '.jpg'

    # Only continue if we haven't already processed this image.
    if not os.path.exists(local_jpg_loc):
        # Get the jpg itself
        response = urllib2.urlopen(m.group(1))
        jpg = response.read()
        # Write the jpeg to the directory
        f = open(local_jpg_loc, 'w')
        f.write(jpg)
        f.close()
        call(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", "file://" + local_jpg_loc.strip(')')])
        print "There's a new pun for you! :D"

if __name__ == "__main__":
    main(sys.argv)
