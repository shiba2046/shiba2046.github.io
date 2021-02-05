---
layout: default
title: Notes on Windows Subsystem Linux
permalink: /wsl/
---

# Run graphical with X

[Notes](https://techcommunity.microsoft.com/t5/windows-dev-appconsult/running-wsl-gui-apps-on-windows-10/ba-p/1493242)

1. Install VcXserv X Server
   https://sourceforge.net/projects/vcxsrv/

2. Set DISPLAY

  ```bash
  export DISPLAY="`grep nameserver /etc/resolv.conf | sed 's/nameserver //'`:0"

  export DISPLAY="`sed -n 's/nameserver //p' /etc/resolv.conf`:0"

  export DISPLAY=$(ip route|awk '/^default/{print $3}'):0.0

  echo $DISPLAY
  ```
3. Create a .xsession
   
  ```
  echo xfce4-session > ~/.xsession
  ```