# Hardware Desk Timer

## Emulating PyImgui Environment in Vagrant

For local PyImgui "emulation" on the timer-ui Vagrant, do the following:

```
cd timer-ui
vagrant up
vagrant ssh
```

Start background Xvfb with GLX support (sized to mimic the screen size):

```
Xvfb :1 -screen 0 480x272x24 +extension GLX +render -noreset &
```

Then run TightVNC Viewer (not same as normal VNC service) on e.g. host Windows and enable listen mode.

Once that is ready, run x11vnc on Vagrant:

```
x11vnc -display :1 -connect 10.0.2.2 &
```

The actual Python script commandline is the same as on the Lichee Pi Nano:

```
DISPLAY=:1 python3 /vagrant/main.py
```

## Testing Scripts on Lichee Pi

First, make a ZIP file (small one hopefully):

```
zip timer-ui.zip *py *png *ttf
```

Start decoder on the Lichee Pi:

```
base64 -d | unzip -
```

Then base64-encode the data and copy-paste the data into serial console:

```
base64 < timer-ui.zip
```

Run the script:

```
DISPLAY=:0 python3 main.py
```
