#!/bin/sh
res=`python ./punday.py`
if [ "$res" != "new pun"]; then
    gsettings set org.gnome.desktop.background picture-uri $res
    echo "A new pun is ready for you :D"
fi
