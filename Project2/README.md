
--------------------------------
|        My System Info        |        
--------------------------------

My System info is a python script that goes through some hardware and networking information on your computer.
It uses a variety of packages, some of which need to be installed in order to function, but I'll get into that later. 

The things my script can do:
1. Spit out a full list of installed programs on your device.
2. Give you a total amount of RAM on the system, as well as the percentage that is being used. 
3. Display your Hostname, Public IP address, ad well as your local IP address.
4. Names the processor in the client, and also gives the number of cores and their percent usage.
5. Does all of the above in one go as an added option.

--------------------------------
|          Motivation          |        
--------------------------------

Seeing the type of programs that we were using in class, I figured this could be something that I could use on a daily basis at work.
Since I work helpdesk, there has sometimes been a need to get a full list of programs on someone's computer, and without knowing cmd
there is no "simple" way to do this. Although there are other ways to do it, I wanted to make my own!

I also wanted to learn how to take user inputs and use them to execute functions. Normal programs can do that, why not mine?

The other functions were added because I wanted to give myself a challenge and a wide range of experience with external and internal python packages.


--------------------------------
|         Installation         |        
--------------------------------

Things you'll need:
1. Python 3.6+ Installed
2. An IDE (I used Visual Studio Code)
3. The following packages:              (If any are not installed for some reason, use the commands below)

subprocess                              pip install subprocess
socket                                  pip install socket
requests                                pip install requests
psutil                                  pip install psutil
platform                                pip install platform
from psutil import virtual_memory
from subprocess import check_output


-------------------------------------------------------------------------------------------------------

Time to actually get some work done.
1. Open up your IDE and change directory to your working directory for the project.
2. In the working directory terminal, install the packages listed above with the corresponding pip install commands.
3. Run the program by typing "python mySysInfo.py" in the working directory terminal without the quotations. 

If all is well and configured properly, you should be able to run the code.
An example of the output that you should see is shown here: ![alt text](https://github.com/Niemiljm/it3038c-scripts/blob/main/Project2/images/OutputAll.png)


--------------------------------
|          References          |        
--------------------------------
I would be lying if I said I did this completely on my own and without guidance from other sources.

1. I used this to learn how to run functions based on input: https://stackoverflow.com/questions/48502404/user-input-to-call-function
2. I used this in order to get the function to retrieve a list of programs on the device: https://www.geeksforgeeks.org/get-a-list-of-installed-softwares-in-windows-using-python/
3. I spent more time than I would like to admit here: https://psutil.readthedocs.io/en/latest/
4. This link taught me how to properly write a README: https://meakaakka.medium.com/a-beginners-guide-to-writing-a-kickass-readme-7ac01da88ab3
5. Also: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#headers








