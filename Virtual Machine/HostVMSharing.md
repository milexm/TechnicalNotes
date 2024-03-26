# Sharing Between Host and Hyper-V Virtual Machine <!-- omit from toc -->

Shared folders and drives are useful for file exchanges between different
machines. This article provides information about sharing **files**,
**folders**, and **drives** between the host and Hyper-V virtual machines.

- [Share Drives Using Virtual Machine Connection](#share-drives-using-virtual-machine-connection)
- [Share Files Folders Drives via the Network](#share-files-folders-drives-via-the-network)
- [References](#references)
- [Machine\](https://www.isumsoft.com/it/share-files-folders-or-drives-between-host-and-hyper-v-virtual-machine/)](#machinehttpswwwisumsoftcomitshare-files-folders-or-drives-between-host-and-hyper-v-virtual-machine)

## Share Drives Using Virtual Machine Connection

A virtual machine connection (VMConnect) allows you to use your computer’s local
resources in a virtual machine. **Enhanced session mode** allows files to be
transferred between virtual machines through clipboard copy-and-paste
operations. perform the steps described at this
location: [Share Drives Using Virtual Machine
Connection](https://www.isumsoft.com/it/share-files-folders-or-drives-between-host-and-hyper-v-virtual-machine/#method1)

## Share Files Folders Drives via the Network

In Windows OS, files and folders can be shared across the network, allowing
desktops and laptops to access information without physically accessing the
computer. For example, users may share an entire document or video folder, and
anyone else with access can open these files, edit and save them – even remove
them if permissions permit. Perform the steps described at this location: [Share
Files Folders Drives via the
Network](https://www.isumsoft.com/it/share-files-folders-or-drives-between-host-and-hyper-v-virtual-machine/#method2).

> [!IMPORTANT] If you want to remove or add a drive or any other resource, in
> Powershell run the following command: 
> `VMConnect.exe <your computer name> <your virtual machine name>/edit`.
> For example: `VMConnect.exe MIKEPCDELL VM_Windows_10/edit`.
> See also [Edit VM
> Settings](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/learn-more/Use-local-resources-on-Hyper-V-virtual-machine-with-VMConnect#edit-vmconnect-settings). 

## References

- [Share Files, Folders or Drives Between the Host and Hyper-V Virtual
  Machine](https://www.isumsoft.com/it/share-files-folders-or-drives-between-host-and-hyper-v-virtual-machine/)
- 