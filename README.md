# Robotics2019
2019 KPCA Robotics camp

## Lecture link
1. https://drive.google.com/file/d/1PYVgTv0V-3Wq4Mi0ZzVAdfaubBaJthgS/view?usp=sharing

## Voice recorder
1. https://drive.google.com/file/d/1wW1tQJzWGRO_LDEuqrxqr3qHQIGCY1PC/view?usp=sharing

## Purchase list
1. [RobotCar] https://www.amazon.com/gp/product/B07Q3RQCQS/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1
2. [RaspberryPi3B+] https://www.amazon.com/gp/product/B07BC6WH7V/ref=ppx_yo_dt_b_asin_title_o05_s01?ie=UTF8&psc=1
3. [SD card] https://www.amazon.com/gp/product/B073JWXGNT/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1
4. [Charger] https://www.amazon.com/gp/product/B01D9TUL8Y/ref=ppx_yo_dt_b_asin_title_o05_s01?ie=UTF8&psc=1

## RaspTank manual
1. https://www.adeept.com/video/static1/itemsfile/Manual_Adeept_RaspTank_V1_2.pdf
2. https://drive.google.com/file/d/1OSZE5E2jvKWPw1DHyuOg5mW2dPT2_BG7/view?usp=sharing

## RaspTank source code
1. https://github.com/adeept/Adeept_RaspTank

## Python tutorials (pdf)
1. https://bugs.python.org/file47781/Tutorial_EDIT.pdf
2. http://anh.cs.luc.edu/python/hands-on/3.1/Hands-onPythonTutorial.pdf
3. https://www.tutorialspoint.com/python3/python_tutorial.pdf
4. http://tdc-www.harvard.edu/Python.pdf

## Python installation (Windows)
1. https://www.python.org/downloads/windows/
2. Latest Python 3 Release - Python 3.8.1 (12/23/2019)
3. Windows x86-64 executable installer
4. Ctl+R & cmd
5. > py

## Python3 set path
1. Right click "This PC"
2. Click Properties
3. Advanced system settings
4. Environment Variables
5. System variables (below)
6. Double click "Path"
7. Click "New"
8. Add C:\Users\"Your user name"\AppData\Local\Programs\Python\Python38
9. Add C:\Users\"Your user name"\AppData\Local\Programs\Python\Python38\Scripts
10. Open terminal and type "python" and "pip" to test

## Notepad++ installation
1. https://notepad-plus-plus.org/downloads/
2. Notepad++ 7.8.2 release (12/23/2019)
3. Download 64-bit x64
4. Installer | GPG Signature << click "Installer"
5. Run installer

## TightVNC viewer installation
1. https://www.tightvnc.com/download.php
2. Installer for Windows (64-bit)
3. setting
  - click "Connection Options" icon (finger shape)
  - Format and encoding
    - Preferred encoding: Tight
    - Allow JPEG, set image quality (quality 2)

## SSH connection to Raspberry pi at Window10
1. Ctl+R & cmd
2. ssh id@ip_address & password

## Raspberry pi static ip address setting
1. open /etc/dhcpcd.conf with text editor (sudo required)
2. add following lines
  - interface wlan0
  - static ip_address=192.168.1.100/24
  - static routers=192.168.1.1
  
## Raspberry pi X11 display setup for GUI
1. xauth list $DISPLAY 
2. pi:10 mit-magic-cookie-1 4d22408aga55sad1ccd165723g77923ae
3. echo $DISPLAY
4. xauth add localhost:10.0 mit-magic-cookie-1 4d22408aga55sad1ccd165723g77923ae
  
## Raspberry pi utilities
1. sudo apt-get update
2. sudo apt-get install tightvncserver
3. sudo apt-get install python3-thonny

## Installing (flashing) Raspberry Pi OS (Raspbian) in Windows
1. Go to https://www.raspberrypi.org/downloads/raspbian/
2. Download: Raspbian Buster with desktop (2nd one)
3. Go to https://www.raspberrypi.org/documentation/installation/installing-images/windows.md
4. Insert the SD card into your SD card reader. You can use the SD card slot if you have one, or an SD adapter in a USB port. Note the drive letter assigned to the SD card. You can see the drive letter in the left hand column of Windows Explorer, for example G:
5. Download the Win32DiskImager utility from the Sourceforge Project page as an installer file, and run it to install the software.
6. https://sourceforge.net/projects/win32diskimager/
7. Run the Win32DiskImager utility from your desktop or menu.
8. Select the image file you extracted earlier.
9. In the device box, select the drive letter of the SD card. Be careful to select the correct drive: if you choose the wrong drive you could destroy the data on your computer's hard disk! If you are using an SD card slot in your computer, and can't see the drive in the Win32DiskImager window, try using an external SD adapter.
10. Click 'Write' and wait for the write to complete.
11. Exit the imager and eject the SD card.
12. Insert microSD card into Raspberry Pi.
13. Start Raspberry Pi.

## Raspberry pi setup for RaspTank
### SSH and Remote desktop
- How to add a network to make Raspberry pi automatically connect to the network when it books up.
  - Connect power, hdmi port to monitor, keyboard and mouse.
  - Boot up raspberry pi.
  - Open Terminal
  - $sudo raspi-config
  - 2. Network Options
  - N2 Wi-fi
  - Please enter SSID: put your wifi name
  - Please enter passphrase. Leave it empty if none: put your wifi password
  - Finish
  - Check your ip address: $ifconfig
  - Check ip address of wlan0 (ex. 192.168.1.100)
  - Reboot for test
- SSH connection from your laptop
  - Now, you don't need monitor, keyboard, and mouse
  - In your laptop, open terminal (or putty if your terminal don't have ssh)
  - $ssh pi@192.168.1.xx (Raspberry pi ip address)
  - $password: raspberry
  - You can see: New 'X' desktop is raspberrypi:3
  - Run TightVNC viewer
  - Use the ip address and the xdesktop number: (ex. 192.168.1.100:3)
  - Now, you can see Raspberry pi screen in your laptop!!
### Installation of basic libraries
- Open terminal
- $git clone https://github.com/adeept/Adeept_RaspTank.git
- $sudo python3 Adeept_RaspTank/setup.py
- Now, it takes several minutes to install all related libraries
### Download test code
- Open terminal
- $git clone https://github.com/gwcheon/Robotics2019
- $cd Robotics2019/src
### LED example
- Open terminal
- $cd Robotics2019/src
- $thonny & (You have to put ampersand '&' after thonny, Text editor similar to notepad++)
- Now, thonny program is open
- Open source code: File > Open and navigate to LED.py (pi/Robotics2019/src/LED.py)
- Go back to terminal
- $sudo python3 LED.py
