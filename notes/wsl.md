---
layout: default
title: Notes on Windows Subsystem Linux
permalink: /wsl/
---

# WSL HOST IP
```bash
export WSL_HOST=`grep nameserver /etc/resolv.conf| cut -d ' ' -f 2`
export PROXY=$WSL_HOST:7890
```

# Set Proxy function
```bash
proxy(){
  case $1 in
  on)
    export http_proxy=http://$PROXY
    export https_proxy=https://$PROXY
    ;;
  off)
    unset http_proxy
    unset https_proxy
    ;;
  *)
    echo "Usage: proxy on|off"
    echo http_proxy=$http_proxy
    echo https_proxy=$https_proxy
    ;;
  esac
}
```
# Run graphical with X

[Notes](https://techcommunity.microsoft.com/t5/windows-dev-appconsult/running-wsl-gui-apps-on-windows-10/ba-p/1493242)

1. Install VcXserv X Server
   https://sourceforge.net/projects/vcxsrv/

2. Set DISPLAY

  ```bash

  # Any one would work
  export DISPLAY="`grep nameserver /etc/resolv.conf | sed 's/nameserver //'`:0"

  export DISPLAY="`sed -n 's/nameserver //p' /etc/resolv.conf`:0"

  export DISPLAY=$(ip route|awk '/^default/{print $3}'):0.0

  echo $DISPLAY
  ```
3. Create a .xsession
   
  ```
  echo xfce4-session > ~/.xsession
  ```


# ADB send text

Need replace space ` ` with `%s`
```bash
# ADB send text
ast(){
  adb shell input text "${1/ /%s}"
}

# Adb send file
asf(){
  adb push ${$1} /sdcard/Download/
}
```


# thefuck slow in ZSH

```bash
echo "excluded_search_path_prefixes = ['/mnt/']" >> ~/.config/thefuck/settings.py
```