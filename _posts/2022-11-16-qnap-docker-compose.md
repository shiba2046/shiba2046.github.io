---
date: 2022-11-16
categories: qnap
title: QNAP Container Station Docker Compose
layout: post
---

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


