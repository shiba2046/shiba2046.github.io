---
layout: default
title: Notes on Linux
permalink: /linux/
---


A collection of my notes while using Linux

# VIM sudo write
`:w !sudo tee %`

# Ubuntu设置

## 初始安装

1. 替换清华源

  修改 `/etc/apt/sources.list`，替换 `archive.ubuntu.com` 为 `mirrors.tuna.tsinghua.edu.cn`

  ```bash
  $ sudo sed -i 's/archive\.ubuntu\.com/mirrors\.tuna\.tsinghua\.edu\.cn/' /etc/apt/sources.list
  $ sudo apt -y update
  $ sudo apt -y upgrade
  ```

2. 从LTS升级到最新版
   
   开始之后需要很长时间！

  ```bash
  $ sed -i 's/lts/normal/' /etc/update-manager/release-upgrades
  $ sudo do-release-upgrade
  ```
3. 检查Ubuntu版本

  ```bash
  $ lsb_release -a
  ```
4. 改hostname
  ```bash
  $ sudo hostnamectl set-hostname NEW_HOST_NAME
  ```

## 安装KVM虚拟机

  教程 [Link](https://www.tecmint.com/install-kvm-on-ubuntu/)

1. Check virtualization support in Ubuntu

  ```bash
  $ sudo apt -y install cpu-checker
  $ sudo kvm-ok
  ```
2. Install KVM

  ```bash
  $ sudo apt install -y qemu qemu-kvm libvirt-daemon libvirt-clients bridge-utils virt-manager
  $ sudo systemctl status libvirtd

  # If not enabled
  $ sudo systemctl enable --now libvirtd

  # Check if KVM modules are loaded
  $ lsmod | grep -i kvm
  ```

3. Create a VM
  ```bash
  virt-manager
  ```

  If no Xwin
  ```bash
  export DISPLAY={desktop_ip}:0
  ```
