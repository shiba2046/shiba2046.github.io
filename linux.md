---
layout: default
title: Notes on Linux
permalink: /linux/
---


A collection of my notes while using Linux

# VIM sudo write
`:w !sudo tee %`

# Ubuntu安装

1. 替换清华源

  修改 `/etc/apt/sources.list`，替换 `archive.ubuntu.com` 为 `mirrors.tuna.tsinghua.edu.cn`

  ```
  $ sudo sed -i 's/archive\.ubuntu\.com/mirrors\.tuna\.tsinghua\.edu\.cn/' /etc/apt/sources.list
  $ sudo apt update
  $ sudo apt -y upgrade
  ```

2. 从LTS升级到最新版

  ```
  $ sed -i 's/lts/normal/' /etc/update-manager/release-upgrades
  $ sudo do-release-upgrade
  ```



new ssh port 1022