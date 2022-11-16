---
layout: default
title: "QNAP笔记"
permalink: /qnap/
---

# Hardware

CPU: J3455 

[为 Container Station 更换镜像](http://einverne.github.io/post/2020/01/qnap-docker-registry-mirror.html)
[替换默认 shell 为 zsh](http://einverne.github.io/post/2019/05/qnap-change-default-login-shell-to-zsh.html)


# cd into QPKG package folder
```
cd `getcfg QDK Install_Path -f /etc/config/qpkg.conf` 
```

# Clash config
```bash
#!/bin/sh
curl https://sub.chiba.bar/link/clash -o clash
#sed -i s/127\.0\.0\.1:9090/0\.0\.0\.0:9090/ clash
#sed -i s/allow-lan:\ false/allow-lan:\ true/ clash
#ed -i s/dns\:/external-ui:\ \"\\/yacd\"\\ndns\:/ clash # Add webui


#docker restart clash
#sleep 10

curl localhost:7090/configs -X PUT -d '{"path": "/root/.config/clash/config.yaml"}'

# curl localhost:7090/proxies/Proxy -X PUT -d '{"name":"By Speed"}'
# curl localhost:7090/proxies/Domestic -X PUT -d '{"name":"DIRECT"}'
# curl localhost:7090/proxies/Others -X PUT -d '{"name":"DIRECT"}'
# curl localhost:7090/proxies/AdBlock -X PUT -d '{"name":"REJECT"}'
# curl localhost:7090/proxies/AsianTV -X PUT -d '{"name":"DIRECT"}'
# curl localhost:7090/proxies/GlobalTV -X PUT -d '{"name":"Proxy"}'
# curl localhost:7090/proxies/Telegram -X PUT -d '{"name":"Proxy"}'
# curl localhost:7090/proxies/Speedtest -X PUT -d '{"name":"DIRECT"}'
# curl localhost:7090/proxies/Microsoft -X PUT -d '{"name":"DIRECT"}'
```


# Container Station 脚本备份

## Clash
```yaml
version: '3'
services:
  clash:
    image: dreamacro/clash:latest
    container_name: clash
    # image: junxy/clash
    volumes:
      - /share/programs/clash/config.yaml:/root/.config/clash/config.yaml
      # dashboard volume
      # - ./ui:/ui
    ports:
      # 7890 - http
      # 7891 - socks
      - "7890:7890"
      - "7891:7891"
      # If you need external controller, you can export this port.
      - "9090:9090"
      # - "5353:53"
      # - "7081:80"
    restart: always
    # When your system is Linux, you can use `network_mode: "host"` directly.
    # network_mode: "bridge"
    # network_mode: host

```


## Jellyfin
```yaml
version: "3"
services:
  jellyfin:
    image: jellyfin/jellyfin:latest
    container_name: jellyfinhw
    environment:
    - TZ=Asia/Shanghai
    - PGID=1000
    - PUID=100
    - WEBUI_PORT=8096
    volumes:
      - /share/programs/jellyfin/config:/config
      - /share/programs/jellyfin/cache:/cache
      - /share/CACHEDEV1_DATA/Multimedia:/share/CACHEDEV1_DATA/Multimedia
      - /share/CACHEDEV1_DATA/PhotoStore:/share/CACHEDEV1_DATA/PhotoStore
      - /share/CACHEDEV2_DATA/Porn:/share/CACHEDEV2_DATA/Porn
    devices:
      - /dev/dri/renderD128:/dev/dri/renderD128
    restart: unless-stopped
    network_mode: host
```



# Build own QPKG package

## 1. Download QDK
   [Link](http://wiki.qnap.com/wiki/QPKG_Development_Guidelines)

## 2. Install `QDK_2.2.4.qpkg`
## 3. Build QPKG

1. Generate enviroment
```bash
$ cd `getcfg QDK Install_Path -f /etc/config/qpkg.conf` 
$ qbuild --create-env QPKG_NAME
$ cd QPKG_NAME
$ ls
```
2. Configure QPKG

    Edit the content of `qpkg.cfg`
    - `QPKG_NAME`: Name of the QPKG
    - `QPKG_VER`: Version
    - `QPKG_AUTHOR`: Author
    - etc

3. Customize QPKG routines

    Content of file `package_routines`

    - `pkg_pre_install()`
    - `pkg_install()`
    - `pkg_post_install()`
    - `PKG_PRE_REMOVE`
    - `PKG_MAIN_REMOVE`
    - `PKG_POST_REMOVE`

    Content of file `shared/QPKG_NAME.sh`

    - `Start`
    - `Stop`

4. Add files

    Put files in below folders:

    - `shared/`: Platform-independent files
    - `x86_64/`: etc: Platform-dependent files
    - `icons/`: icon files
    - `config/`: config files

5. Build QPKG file

    ```bash
    $ qbuild
    $ cd build/
    $ ls
    ```
