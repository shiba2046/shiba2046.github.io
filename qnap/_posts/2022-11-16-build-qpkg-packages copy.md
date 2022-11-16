---
date: 2022-11-16
categories: qnap
title: Build QNAP QPKG Packages
layout: post
---


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
