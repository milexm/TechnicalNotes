# Getting Started with Python in VS Code <!-- omit from toc -->

- [1. Introdcuction](#1-introdcuction)
  - [1.1. Windows](#11-windows)
- [2. Create a virtual environment](#2-create-a-virtual-environment)
- [3. Activate the environment](#3-activate-the-environment)
- [4. Hello World example](#4-hello-world-example)
- [5. References](#5-references)


## 1. Introdcuction

Along with the Python extension, you need to install a Python interpreter. Which interpreter you use is dependent on your specific needs, but some guidance is provided below.

### 1.1. Windows

Install Python from [python.org](https://www.python.org/downloads/). Use the Download Python button that appears first on the page to download the latest version.

Note: If you don't have admin access, an additional option for installing Python on Windows is to use the Microsoft Store. The Microsoft Store provides installs of [supported Python versions](https://apps.microsoft.com/store/search?publisher=Python%20Software%20Foundation).

For additional information about using Python on Windows, see Using [Python on Windows at Python.org](https://docs.python.org/3.9/using/windows.html).


## 2. Create a virtual environment

A best practice is to use a **project-specific virtual** environment. Once
you activate that environment, any packages you then install are
isolated from other environments, including the global interpreter
environment, reducing many complications that can arise from conflicting
package versions. You can create non-global environments in VS Code
using Venv or Anaconda with Python: Create Environment.

1. Create a directory that must contain your virtual environment, for example `C:\.venvs`. 
1. Navigate to that directory just created and execute the following command:  C:\.venvs> `python -m venv workenv`. This creates the `worknenv` diectory that contains the virtual environment. 

> [!NOTE]
> I found useful to create a global `.venvs` directory to contain several Pythpn environments to share among projects.

## 3. Activate the environment

Before activating the desired environment, assure that the terminal default is a **command console**. Perform the following steps:

1. Select `Ctrl + Shift + P` to open the command palette.
1. Type **profile** in the searcher.
1. Select **Terminal: Select Default Profile**.
1. Select **Command Prompt**.
The next time you open the terminal you should see 'CMD' instead of 'PowerShell'.

To activate the anvironment perform the following steps:

1. Open the command palette and enter **python**.
1. In the drop-down meenu select **Enter interpreter path...**. In our example, the path is: `C:\.venvs\workenv\Scripts\python.exe`. 
1. The terminal displays prompt similar to this: `(workenv) C:\GitHub\milexm\TechnicalNotes>`. The prefix `(workenv)` signifies that the selected environment is activated. 
1. Enter `deactivate` to exit the environmnent. Conversely enter `activate` to activate the environment.

## 4. Hello World example

Let's check now if the virtual environment is working correclty. 

1. Create the `helloworld.py` Python program, as shown in [helloworld](helloworld.py).
1. Activate the `workenv` as described before.  
1. Open a terminal window, change directory to the one that contains the program: `(workenv) C:\GitHub\milexm\TechnicalNotes\Tools\Visual Studio Code>`.
1. Execute the command: `python helloworld.py`.

## 5. References

- [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial#_install-a-python-interpreter)