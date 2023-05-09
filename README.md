# Hurricane-Visualization
##### Authors: Matt Streicher and Kunal Manjare
##### University of Utah CS5635/6636 Visualization for Scientific Data

This repository holds the results of our final project on Hurricane Visualization. In order to load the .pvsm files within the state_files folder,
you will need to dowload ParaView https://www.paraview.org/. 

In addition, the Hurricane Isabel dataset is required and can be found at http://vis.computer.org/vis2004contest/data.html.
The Hurricane Katrina data is provided as a .vts file.

We recommend using the Python scripts in order to download, and convert the Isabel data. Once downloaded and converted you should have 625 .raw files
There are multiple variables, each with 48 time steps. They are labeled as VARfxx. Where VAR is replaced by the variable name and xx is the time step from 01-48.
Each file is 500x500x100 except for HGTData. HGTData represents the ground and is 500x500x1. 

This project was one of six projects to be nominated for Best Project in the class.

You can read our final report for more information on how we handled the data and interpreted the results.
