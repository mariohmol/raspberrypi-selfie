

## Emulating

First install a VM to have a RaspberryPi emulating in your enviroment, in my case OSX. So install the emulator, QEMU:

* brew install qemu

Download and unzip raspbien version wheezy:

* http://director.downloads.raspberrypi.org/raspbian/images/2012-12-16-wheezy-raspbian/2012-12-16-wheezy-raspbian.zip

Download compatible kernel in same folder of raspbien:

* https://raw.githubusercontent.com/dhruvvyas90/qemu-rpi-kernel/master/kernel-qemu-3.10.25-wheezy


The command to start emulator at first time is:

* qemu-system-arm -kernel kernel-qemu-3.10.25-wheezy -cpu arm1176 -m 256 -M versatilepb -no-reboot -serial stdio -append "root=/dev/sda2 panic=1 rootfstype=ext4 rw init=/bin/bash" -hda 2012-12-16-wheezy-raspbian.img


Follow the procedure described here, steps 1 to 6:

* https://github.com/dhruvvyas90/qemu-rpi-kernel/wiki

After that, the command line to start emulator that goes direclty to X is:

* qemu-system-arm -kernel kernel-qemu-3.10.25-wheezy -cpu arm1176 -m 256 -M versatilepb -no-reboot -serial stdio -append "root=/dev/sda2 panic=1 rootfstype=ext4 rw" -hda 2012-12-16-wheezy-raspbian.img


See how it should open, with keyboard and mouse working:

![alt tag](https://raw.github.com/mariohmol/raspberrypi-selfie/master/docs/emulator.png)



### Other links

* https://gist.github.com/JasonGhent/e7deab904b30cbc08a7d
* http://raspberrypi.stackexchange.com/questions/7081/how-to-successfully-emulate-rpi-on-osx/15891#15891?newreg=4d923ddf0b024600978c76445943dd4d


Kernel version must match the version for raspbian image version.

* https://github.com/dhruvvyas90/qemu-rpi-kernel/wiki
* https://github.com/polaco1782/raspberry-qemu
* https://github.com/cantora/qemu-arm-rpi-kernel

Compile manually:

* https://github.com/raspberrypi/linux



----



## Resize Image

If you need a image with more free space, using MacOS as guest in VM, you need to 

Install Macports, it will install packages to resize image:

* https://guide.macports.org/#installing.macports

TO install the package to resize, called e2fsprogs:

* /opt/local/bin/port e2fsprogs

With all libs, follow the procedure:

* http://raspberrypi.stackexchange.com/questions/4943/resize-image-file-before-writing-to-sd-card



## Install in raspberry:

There is a step by step here:

* https://www.raspberrypi.org/documentation/installation/installing-images/

As i'm using MAC:

* https://www.raspberrypi.org/documentation/installation/installing-images/mac.md

Basically, input your SD card then:

* run df -h and see the dev number for your sdcard, in my case were /dev/disk3
* Then unmount: diskutil unmount /dev/disk3
* After that store your img in SD: sudo dd bs=1m if=2012-12-16-wheezy-raspbian.img of=/dev/disk3


### Other links

* https://github.com/debian-pi/raspbian-ua-netinst
* http://blog.smalleycreative.com/linux/setup-a-headless-raspberry-pi-with-raspbian-jessie-on-os-x/


