
--------------------------------
|            Lab 7             |        
--------------------------------

For lab 7 I chose to work with MatPlotLib, which is a data visualization plugin for python!
I was able to create a number of different graphs and plot data on them by following the instructions of a youtube tutorial which I will credit below.
One of the cool things that this software uses is called JupyterLab, which is a web-based software that works as its own IDE and calculator.

--------------------------------
|          Motivation          |        
--------------------------------

I have had no experience when it comes to using plugins for Python, and this process definitely made me troubleshoot and think somewhat critically.
I'm sure there could have been a flashier plugin to use, but I can actually see myself using this plugin in the future when I get out into the real world.
My sister is a data analyst contractor for some big clothing lines, and I wanted to show her what this software could do, especially since she is learning Python as well!

--------------------------------
|         Installation         |        
--------------------------------

Things you'll need:
1. Python 3+
2. Pip3
3. A virtual environment setup in your working directory.
4. JupyterLab (There is more than one version, and JupyterLab worked the best for me)
5. MatPlotLib
6. Any kind of numerical data. (I have data setup in my script if you simply want to use that)

-------------------------------------------------------------------------------------------------------

Time to actually get some work done.
1. Open up your IDE and change directory to your working directory for the project. (I use Visual Studio Code)
2. In the working directory and within your virtual environment, execute these commands separately and without quotations.
    "python -m pip install -U pip"
    "python -m pip install -U matplotlib"
    "pip install jupyterlab"
3. In the working directory and within your virtual environment, execute the following command without quotations to start JupyterLab.
    "jupyter-lab"
4. If all of the necessary libraries are installed, it should prompt you to choose how to open an .html file, or it will open in your browser under the localhost:8888 url.
5. There are two ways to select the script,
    a. Select it from the directory panel on the left hand side of the JupyterLab webapp.
    b. Selecting 'File' from the top left, and browsing your computer to open the script.
6. Once the file is open, you can re-run the script by either
    a. Clicking anywhere on the code and pressing "Shift + Enter"
    b. Clicking on the run icon within the banner at the top of the screen.
If all is well and configured properly, you should be able to run the code.

Example 1: An example of a simple comparative graph: ![alt text](https://github.com/Niemiljm/it3038c-scripts/blob/main/Python/Lab7/Images/FirstGraph.png "FirstGraph")
Example 2: The two lines that were in example 1, but in separate graphs: ![alt text](https://github.com/Niemiljm/it3038c-scripts/blob/main/Python/Lab7/Images/SecondGraph.png "SecondGraph")
Example 3: 6 Generated graphs, 2 of which have data in them based on coordinates: ![alt text](https://github.com/Niemiljm/it3038c-scripts/blob/main/Python/Lab7/Images/ThirdGraph.png "ThirdGraph")
Example 4: A cool looking colormap that was generated: ![alt text](https://github.com/Niemiljm/it3038c-scripts/blob/main/Python/Lab7/Images/FourthGraph.png "FourthGraph")

To exit the program use (Control + C) in the terminal window.

--------------------------------
|           Credits            |        
--------------------------------

I would be lying if I said I did this completely on my own and without guidance from other sources.

1. This link taught me how to get started with the application setup: https://jupyter.org/install and https://matplotlib.org/stable/users/installing.html
2. MatPlotLib has some amazing documentation and tutorials, this one expecially for creating a colormap: https://matplotlib.org/stable/gallery/color/custom_cmap.html#sphx-glr-gallery-color-custom-cmap-py
3. Academind provided a great walkthrough and provided some simple stock data to manipulate within these graphs: https://www.youtube.com/watch?v=qErBw-R2Ybk
4. This link taught me how to properly write a README: https://meakaakka.medium.com/a-beginners-guide-to-writing-a-kickass-readme-7ac01da88ab3
    Also: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#headers







