---
# date: 2022-11-16
categories: qnap
title: Update QNAP firmware manually
# layout: post
---

1. Create tmpfs space and mount as `/mnt/update`

```bash
sudo bash
mkdir -p /mnt/update 
mount -t tmpfs -o size=50% none /mnt/update
cd /mnt/update
```

2. Find the link to firmware [Link](https://www.qnap.com.cn/zh-cn/download?model=ts-453bmini&category=firmware)


3. Download the firmware file to the NAS:

```bash
# /mnt/update
wget https://download.qnap.com.cn/Storage/TS-X53B/TS-X53B_20221022-5.0.1.2194.zip
```

4. Unzip the file

```bash
# /mnt/update
unzip TS-X53B_20221022-5.0.1.2194.zip
```

5. Run the update script

```bash
# /mnt/update
/etc/init.d/update.sh TS-X53B_20221022-5.0.1.2194.img
```

6. Reboot

```
reboot
```