# raspberrypi-selfie

Using RaspberryPi, a Camera and a Push Button to have a Selfie widget that takes a picture from the user and automatically post in a wordpress blog in the web. 


## Emulating

See all steps to emulate raspberrypi in your MacOS

[Absolute README link](https://github.com/mariohmol/raspberrypi-selfie/blob/master/Emulating.md)



See how it should open, with keyboard and mouse working:

![alt tag](https://raw.github.com/mariohmol/raspberrypi-selfie/master/docs/emulator.png)


## Development

https://www.raspberrypi.org/documentation/linux/software/python.md

Post in Wordpress:

* http://python-wordpress-xmlrpc.readthedocs.org/

Camera

* http://www.rs-online.com/designspark/electronics/knowledge-item/raspberry-pi-camera-setup
* http://blog.gbaman.info/?p=150

Libs:

* http://www.pyimagesearch.com/2015/02/23/install-opencv-and-python-on-your-raspberry-pi-2-and-b/ 


## Configuration

You need to define WP Url , User and Password to connect via XMLRPC:

* export WP_LINK=http://yourblog.com/xmlrpc.php
* export WP_USER=admin
* export WP_PASS=MYpass

## TODO: 

* Make it read a camera and show in screen
* Button to make an action
* This action take a picture and save local
* Take this local picture and send as a post to WP
* Have to connect using local wifi

