# Virtual Machines <!-- omit from toc -->

This folder describes **virtual machines**, their configuration, and their use.
Virtual machines allow you to run an operating system in an app window on your
desktop that behaves like a full, separate computer.

> [!NOTE]
> Virtual machines allow you to run an operating system in an application window on your desktop that behaves like a full, separate computer. You can use them to play around with different operating systems, run software your main operating system can't, and try out apps in a safe, sandboxed environment.

There are several good free virtual machine (VM) apps out there, which makes setting up a virtual machine something anybody can do. You'll need to install a VM app and have access to installation media for the operating system you want to install. We are going to use [Microsoft Hyper-V](https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/about/). 


## Reasons to use virtualization

Virtualization allows you to:

- Run software that requires an older version of Windows or non-Windows operating systems.
- Experiment with other operating systems. Hyper-V makes it very easy to create and remove different operating systems.
- Test software on multiple operating systems using multiple virtual machines. With Hyper-V, you can run them all on a single desktop or laptop computer. These virtual machines can be exported and then imported into any other Hyper-V system, including Azure.
- In my case, I want to create a work environment that does not interfere with the applications on my home computer. 
  
## Next Steps

1. [Install Hyper-V on Windows 10](https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v)
1. [Create a Virtual Machine with Hyper-V on Windows 10 Creators Update](https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/quick-create-virtual-machine) 
   1. [Windows 10 Creators Update (Windows 10 version 1703)](https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/quick-create-virtual-machine#windows-10-creators-update-windows-10-version-1703)
2. [Sharing Between Host and Hyper-V Virtual Machine](../Virtual%20Machine/HostVMSharing.md)

## References

- [Microsoft Hyper-V](https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/about/)
- [Beginner Geek: How to Create and Use Virtual Machines](https://www.howtogeek.com/196060/beginner-geek-how-to-create-and-use-virtual-machines/)