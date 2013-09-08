#!/bin/python
import sys, urllib2, re, os

def main(argv):

    # If the punday folder doesn't exist, make it!
    userpath = os.path.expanduser('~/.punday')
    if not os.path.exists(userpath):
        os.mkdir(userpath)

    response = urllib2.urlopen('http://mondaypunday.com')
    html = response.read()
    m = re.search('wp-image-(\d+).+?src="([^"]+)"', html)

    local_jpg_loc = userpath + '/' + m.group(1) + '.jpg'

    # Only continue if we haven't already processed this image.
    if not os.path.exists(local_jpg_loc):
        # Get the jpg itself
        response = urllib2.urlopen(m.group(2))
        jpg = response.read()
        # Write the jpeg to the directory
        f = open(local_jpg_loc, 'w')
        f.write(jpg)
        f.close()
        print local_jpg_loc
    else:
        print 'no new pun'

if __name__ == "__main__":
    main(sys.argv)
