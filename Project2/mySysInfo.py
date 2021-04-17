import subprocess
import socket
import requests
import psutil
import platform
from psutil import virtual_memory
from subprocess import check_output



class the_action(object):

    # ProgramList will spit out a program list | IP will display the device ipconfig | Memory will display the total memory and free memory | CPU will display the CPU info | All displays all of these.
    def ProgramList(run):
        print("One moment while I grab that list for you!")
        print("-------------------------------------------------------------")
        ProgramList = subprocess.check_output(['wmic', 'product', 'get', 'name'])
        plist = str(ProgramList)

        try:
            for a in range(len(plist)):
                print(plist.split("\\r\\r\\n")[6:][a])

        except IndexError as e:
            print("-------------------------------------------------------------")
            print("|                   Your list is above!                     |")
            print("-------------------------------------------------------------")
            run.__init__()

    # Memory will give a total amount of RAM in GB as well as the current % usage of RAM.
    def Memory(run):
        ram = virtual_memory()
        ramTot = ram.total/(1024.**3)
        ramPer = ram.percent
        print("-------------------------------------------------------------")
        print(ramTot, "GB of RAM")
        print(ramPer, "percentage used currently")
        print("-------------------------------------------------------------")
        run.__init__()

    # IPList will give you a few bits of information about your networking
    def IPList(run):
        hostname = socket.gethostname()
        localIP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        localIP.connect(("8.8.8.8", 80))                                        # This opens a socket to google, to ensure that the NIC we're testing can connect to the internet. Otherwise you may get a 127 address, which we don't want.
        publicIP = requests.get("http://wtfismyip.com/text").text               # This reaches out to wtfismyip to get your public facing IP address
        print("-------------------------------------------------------------")
        print(hostname, " Is your hostname")                                    # This simply gets your hostname, since you can get your localIP from the hostname
        print(publicIP, " Is your public IP address")
        print(localIP.getsockname()[0], " Is your local IP address")
        print("-------------------------------------------------------------")
        localIP.close()                                                         # This closes the socket so that is doesn't keep running.
        run.__init__()

    # CPUList is the function that will output the name/type of processor your device has, as well as the percentage of usage in each core.
    def CPUList(run):
        for x in range(3):
            CpuUsage = psutil.cpu_percent(interval=1, percpu=True)              # Goes through each core and pulls percentages
        CpuName = platform.processor()                                          # Gets the name of your cpu "Intel64 Family 6 Model 158 Stepping 9, GenuineIntel"
        print("This one can take a little bit of time, don't panic!")
        print("-------------------------------------------------------------")
        print(CpuName, " Is the name of your processor")
        print(CpuUsage, " Is the percentage usage of each CPU Core")
        print("-------------------------------------------------------------")
        run.__init__()

    # AllRun runs everything above in one go. 
    def AllRun(run):
        print("Hang tight, this one might take a second!")          
        ProgramList = subprocess.check_output(['wmic', 'product', 'get', 'name'])   # This is the command to get program list from cmd
        plist = str(ProgramList)
        try:
            for a in range(len(plist)):
                print(plist.split("\\r\\r\\n")[6:][a])                              # Formatting the list into something readable
        except IndexError as e:                                                     # When it fails, stop.
            print("-------------------------------------------------------------")
            print("|               Your program list is above!                 |")
            print("-------------------------------------------------------------")

        # Memory will give a total amount of RAM in GB as well as the current % usage of RAM.
        ram = virtual_memory()
        ramTot = ram.total/(1024.**3)                                           # Makes the RAM total readable by converting it to GB
        ramPer = ram.percent                                                    # Gives current usage data for RAM
        print("-------------------------------------------------------------")
        print(ramTot, "GB of RAM")
        print(ramPer, "percentage used currently")       
        print("-------------------------------------------------------------")

        # IPList will give you a few bits of information about your networking
        hostname = socket.gethostname()
        localIP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        localIP.connect(("8.8.8.8", 80))                                        # This opens a socket to google, to ensure that the NIC we're testing can connect to the internet. Otherwise you may get a 127 address, which we don't want.
        publicIP = requests.get("http://wtfismyip.com/text").text               # This reaches out to wtfismyip to get your public facing IP address
        print("-------------------------------------------------------------")
        print(hostname, " Is your hostname")                                    # This simply gets your hostname, since you can get your localIP from the hostname
        print(publicIP, " Is your public IP address")
        print(localIP.getsockname()[0], " Is your local IP address")
        localIP.close()
        print("-------------------------------------------------------------")

        # CPUList is the function that will output the name/type of processor your device has, as well as the percentage of usage in each core.
        for x in range(3):
            CpuUsage = psutil.cpu_percent(interval=1, percpu=True)              # Goes through each core and pulls percentages
        CpuName = platform.processor()                                          # Gets the name of your cpu "Intel64 Family 6 Model 158 Stepping 9, GenuineIntel"
        print("-------------------------------------------------------------")
        print(CpuName, " Is the name of your processor")
        print(CpuUsage, " Is the percentage usage of each CPU Core")
        print("-------------------------------------------------------------")
        print("Phew!! That was a lot of work!")
        run.__init__()

    #This takes the input from the user
    def __init__(run):
        run.init = input("What would you like to do? (1 = Program, 2 = Memory, 3 = IP, 4 = CPU, 5 = All, 6 = Exit) Please enter a number from the list: ")
        list = [1, 2, 3, 4, 5, 6]

        if run.init == str(1):                                                  # This if statement takes the init input and determines which functions to run (ProgramList, IPList, CPUList, or AllRun)           
            run.ProgramList()
        elif run.init == str(2):
            run.Memory()
        elif run.init == str(3):
            run.IPList()
        elif run.init == str(4):
            run.CPUList()
        elif run.init == str(5):
            run.AllRun()
        elif run.init == str(6):
            print("Thank you come again!")
            exit(0)       
        elif run.init != list:
            print("Please submit a proper input: ") # In the event you try to get smart and submit a letter or invalid character, it will fail and return until you do it right.
            run.__init__()
        
a = the_action(); 