---
layout: post
title: 九号电动自行车速度限制解除
tags: 九号 ninebot 
categories: hack
summary: 九号电动自行车解除速度限制的方法    

hero_image: https://imgweboss.ninebot.com/segway-website/portal/product/webcss/product/powerC/images/cbike-bailv-img.png
hero_darken: true
---

1. 下载BLE Tools

2. 进入手机设置，把九号出行APP的蓝牙权限关闭，再到九号app里面将感应解锁关闭，并且打开提示音；

3. 用感应卡解锁电动车，使电动车处于开机状态，退出九号出行APP后台进程，保证九号出行APP处于退出状态！

4. 打开调试助手后，搜索到的设备名为车辆序列号，即为所需要添加的车辆。一般设备名为 `N*D` 开头；点击设备名称右侧的CONNECT连接自己的电动车;

5. 连接成功后，选择在最下面一栏（Unknown Service）选项，点击最下面向上的箭头，在输入框中输入 `5AA500494692E1388FDE307CC0`；

    注:代码有时会出bug，所以一个代码不行的话换一个试试，对于九号说全系列车应该都可以解除。备用代码如下:

    ```
    5AA5003735192AF380ABF07CC0

    5AA5007057457776656E467A39

    5AA500293612C9288DDF772CC0

    5AA500494692E1388FDE307CC0
    ```

6. 输入完毕后，选择单次发送，数据类型选择HEX，然后点击“写入”，此时电动车会发出“嘟”的声响，按照这个方法重复两次接口。

    注意的是，第一次成功写入是解除15KM/h的限速报警提示音，第二次成功写入是解除25KM/h限速，第三次成功写入就恢复了新国标状态。另外解除限速后仪表显示最高时速还是25KM/h。