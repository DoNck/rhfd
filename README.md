# rhfd
RHFD: Recursive Http Files Downloader

## Description
This is a very simple tool for downloading files from an http server such as Apache.

## Dependencies
Install the dependencies into the current working directory:  
```$ pip install -t ./ -r requirements.txt```  
or add them to the system: ```# pip install -r requirements.txt```

##Example
./rhfd.py "http://mirror.archlinux.ikoula.com/archlinux/iso/2015.08.01/arch/boot/"

RHFD will create and download the following directories and files:

```
boot/
├── i686
│   ├── archiso.img
│   └── vmlinuz
├── intel_ucode.img
├── intel_ucode.LICENSE
└── x86_64
    ├── archiso.img
    └── vmlinuz
```

## Code maturity
Testing is very limited: I just tested this program with one Apache/2.2.22 (Debian) Server instance and the archlinux server from the example. Please report bugs if you find any.
Despite I made this code with love, it is one of my first Python programs, so feel free to suggest improvements.

## TODO
parallel downloads, global progress bar, regex based filtering, volume and speed stats before exiting, find a better name
