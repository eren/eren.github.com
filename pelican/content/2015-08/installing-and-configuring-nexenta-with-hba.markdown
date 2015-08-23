Title: Fixing Boot Problem with NexentaStor on Supermicro Server with LSI 9201-8i HBA Card
Category: System Administration
Tags: nexenta,nexentastor,supermicro,hba,lsi-9201-8i,boot
Date: 2015-08-23

I didn't have time to blog about this when I was working on it. After 1 month of fixing the problem and having a time, I decided to write it.

I spend a couple of hours debugging the boot problem with NexentaStor on supermicro server with LSI 9201-8i HBA card. The LSI card is no longer produced but they can be found on e-bay with a really good price. We had one of those cards that drives our JBOD to be used in Nexenta. This box is simply a medium-sized storage server to which clients connect using iSCSI.

## Configuration and First Trial
The backplane on the server is connected to the first port on the LSI card so that the disks are controlled by it. To be sure absolutely sure, I disabled SATA controller in BIOS. Later, I booted nexenta using a virtual CD (you can mount ISO using IPMI interface of supermicro). The boot process took so long that I thought the server cannot boot from CD when the card is plugged in. However, after waiting a few minutes, it booted successfully.

In the installation screen, I saw all the disks which are controlled by the LSI card. I selected disk 0 and 1 (mirror) to be used for OS installation. NexentaStor did the magic and finished the installation. However, here the problems started.

## Symptoms
After the installation, I rebooted the server and waited for the boot process. However, I got *"no boot disks found"* error just as if it's not installed.

I went to BIOS and checked that the boot order is correct. The first boot device is seen as LSI HBA card. Later, I went to LSI controller and checked the boot device. I saw that there is no boot disk configured in the controller. I checked the boot flag on disk 0, and alternative device for disk 1 (since they're mirrored) and thought that it's going to work. Murphy's law here, it didn't work. I saw the same message again and again.

I thought maybe there is an issue with the GRUB installation on NexentaStor. I tried Ubuntu Server 14.04 and I got the same message. This meant that the problem is not distro-specific, the problem is isolated to the card.

## The Fix
It was clear that the server failed to boot with LSI card, or LSI card couldn't boot the OS using the disks even if they're set in boot mode. I decided to go with the SATA controller on the motherboard. I got 2 SSD disks and connected them to the motherboard's SATA ports, enabled SATA in BIOS and set the boot order to use those SSD disks. After the installation on SSD disks, the box booted fine, problem solved! :)

So at the end, the OS is on different disk controller (motherboard) and all the data disks are controlled by LSI card. I like this setup as OS and data are separate.
