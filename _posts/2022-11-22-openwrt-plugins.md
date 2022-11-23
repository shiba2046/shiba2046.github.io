---
title: 常用Openwrt插件下载
categories: openwrt
summary: |-
    常用的一些Openwrt插件下载
---

# 必备的一些插件

## OpenClash

```bash
REPO="messense/aliyundrive-webdav"
ARCH="x86_64.ipk\|all.ipk"
curl -sL "https://api.github.com/repos/$REPO/releases/latest" | grep "browser_download_url" | cut -d : -f 2,3 | tr -d \" | grep $ARCH | wget -qi -
```


## Aliyun Webdav

```bash
bash
REPO="messense/aliyundrive-webdav"
ARCH="x86_64.ipk\|all.ipk"
curl -sL "https://api.github.com/repos/$REPO/releases/latest" | grep "browser_download_url" | cut -d : -f 2,3 | tr -d \" | grep $ARCH | wget -qi -
```


```bash
find . -name "*aliyun*ipk" -exec rm -f {} \;
curl -sL "https://api.github.com/repos/messense/aliyundrive-webdav/releases/latest" | grep "browser_download_url" | cut -d : -f 2,3 | tr -d \" | grep "x86_64.ipk\|all.ipk" | wget -qi -
find . -name "*ipk" -exec opkg install {} \;
```