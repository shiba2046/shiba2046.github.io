---
categories: github
tags: github openwrt bash
---

用脚本下载 Github 最新的release

```bash
curl -sL "https://api.github.com/repos/messense/aliyundrive-webdav/releases/latest" | \
 grep "browser_download_url" | \
 cut -d : -f 2,3 | tr -d \" | \
 grep "x86_64.ipk\|all.ipk" | \
 wget -qi -
```

```bash
REPO="messense/aliyundrive-webdav"
ARCH="x86_64.ipk\|all.ipk"
curl -sL "https://api.github.com/repos/$REPO/releases/latest" | grep "browser_download_url" | cut -d : -f 2,3 | tr -d \" | grep $ARCH | wget -qi -
```