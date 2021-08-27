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

Then run TightVNC on e.g. host Windows in listen mode.

Once that is ready, run x11vnc on Vagrant:

```
x11vnc -display :1 -connect 10.0.2.2 &
```

The actual Python script commandline is the same as on the Lichee Pi Nano:

```
PYSDL2_DLL_PATH=/usr/lib DISPLAY=:1 SDL_VIDEODRIVER=x11 SDL_NOMOUSE=true python3 /vagrant/pyimgui.py
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
PYSDL2_DLL_PATH=/usr/lib DISPLAY=:0 SDL_VIDEODRIVER=x11 SDL_NOMOUSE=true python3 main.py
```
