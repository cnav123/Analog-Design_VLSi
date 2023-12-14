Source : - The below project is the HW of the Cource in Udemy "Automate LTspice Circuit Simulation Using Python Scripting" by "Prof Ye Zhao PhD"

Link:- https://www.udemy.com/share/102T0i3@QHHo590GPNY5Aecv64IWDrnDLgvUTXJ-pWLnvSNNIskBKGJImYl1mcylInhY8ESK/

In this project I have worked on a Project for Automating the process of Simulation of LTspice circuit Using Python

Step 1:- Create the txt files (netlist) from the given asc file

Step 2:- Use Python to automatically change the variables in .txt files under various combinations of Res1, Cap1, Res2, and Cap2, and save the netlist files as new txt files under subdirectory name “SimFolder”
                  •listRes1 = {1k,10k}, listC1 = {0.1u, 1u}
                  •listRes2 = {1k, 10k}, listC2 = {0.1u, 1u}
                  •For example, a txt file name “Res1=1k_Cap1=0.1u_Res2=1k_Cap2=0.1u.txt”
                  •Make sure no space in the file name!
                  •The total # of files = 16 (= 2^4)
Step 3:- Run each txt files in LTspice batch mode using Python scripting
Step 4:- Import each raw data into Python, and plot the transient analysis results in Python and save as png figures under subdirectory name “FigFolder”
                    • Put the same file name as the title in each figure
                    • For example, a figure name is "Res1=1k_Cap1=0.1u_Res2=1k_Cap2=0.1u.png”
                    • Put legends on each figure
