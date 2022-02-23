# How to mount a drive on Linux

*This is a boiled down version of https://linuxize.com/post/how-to-install-virtualbox-guest-additions-in-ubuntu/*

- Connect the downloaded extensions to the VM by going to Settings>Storage>Right-click Controller>+Optical Drive
- Select “VBoxGuestAdditions.iso” and click Choose
- In the server console do the following:
- sudo apt install build-essential dkms linux-headers-$(uname -r)
- sudo mkdir -p /mnt/cdrom
- sudo mount /dev/cdrom /mnt/cdrom
- cd /mnt/cdrom
- sudo sh ./VBoxLinuxAdditions.run --nox11
- sudo shutdown -r now
