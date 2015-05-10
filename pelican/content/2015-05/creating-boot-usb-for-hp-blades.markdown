Title: Creating Bootable USB For HP Blades (Service Pack)
Category: blog
Tags: hp,blade,usb,spp,illegal opcode
Date: 2015-05-10

HP provides service packs for its blade servers. They are distributed as iso images so you need to either burn the iso file to DVD (slow update) or create a bootable USB (fast). Unfortunately, the guide that HP provides for creating bootable USB does not work under **Ubuntu 14.04** using syslinux version **4.05**. When booted, you get a decent red screen saying **illegal opcode** with CPU registers on the screen.

I realised that the problem is caused by MBR. Somehow, syslinux in Ubuntu 14.04 causes illegal opcode when booted on HP hardware. After digging the internet, I found [this e-mail thread](http://www.syslinux.org/archives/2012-December/019047.html) which discusses the same problem. I didn't apply the exact steps mentioned the URL. Here is how you create bootable USB disk for HP Blades under Ubuntu 14.04.

### Before starting
1. Download SPP iso from HP, mount the ISO [^iso]
2. Get [ms-sys](http://ms-sys.sourceforge.net) utility. If your distribution has it in its repository, you're lucky, install it with the package manager. If not, compile the software.
3. Plug-in your USB drive.

 
### Clean MBR, install syslinux
*!! NOTE !! This part includes important disk operations. Please and please be make sure that you write the correct device name of the USB drive. You can end up with zeroing out your main drive*

Rename sdx with your usb disk path.

```shell
# zero-out mbr
ms-sys -z /dev/sdx

# create msdos label
parted -s /dev/sdx mklabel msdos
    
# write syslinux MBR provided by ms-sys 
ms-sys -s /dev/sdx
```

### Partition the drive
I used **gparted** for partitioning the drive [^2]. Open gparted, select your USB drive, create a new partition, format it with **FAT32**, select **lba** and **boot** flags on the partition.

Install syslinux on the partition.

```
syslinux -i /dev/sdx1
```

### Copy files
Use the following commands to copy files to usb drive. Change the exported settings accordingly to your mount points.

```shell
export HP_SOURCE="/mnt/hpiso"
export HP_USB_DISK="/mnt/usbdisk"
 
rsync -rltDuvh --progress $HP_SOURCE/ $HP_USB_DISK/
 
cp -rf $HP_SOURCE/system/initrd.img $HP_USB_DISK
cp -rf $HP_SOURCE/system/vmlinuz $HP_USB_DISK
cp -rf $HP_SOURCE/system/*.c32 $HP_USB_DISK
cp -rf $HP_SOURCE/system/*.jpg $HP_USB_DISK
cp -rf $HP_SOURCE/system/blacklist $HP_USB_DISK
cp -rf $HP_SOURCE/system/sample.msg $HP_USB_DISK
cp -rf $HP_SOURCE/usb/syslinux.cfg $HP_USB_DISK
 
# HP's vesamenu file gives error. Copy vesamenu from system
cp -f /usr/lib/syslinux/vesamenu.c32 $HP_USB_DISK

sync
```

Now you are ready to go. Plug out the drive and boot your blade. It should automatically start updating.

### Note
I tried this process with **Sandisk Extreme USB 3.0** thumb drive. It booted correctly, but it failed to boot with **Sandisk *Ultra* USB 3.0**. It seems that there is a difference between usb drives. Check your drive if it boots a live linux distribution.

Hope it helps.

[^iso]: You can mount the iso using: mount -o loop DISK.iso [LOCATION]
[^2]: I could have used console commands but gparted seemd easier. You can use your favourite disk partitioning tool but gparted is the tested one in this scenario.

