# Basic Usages

// add structure

## Install packages
The program is written in *python*. Make sure you have a *python 3* in your computer. You also need to install some requirement packages by using these following commands.

 

     $ pip install -r requirements.txt
    
 ## Run the experiments
 Use *python "program_name"* to run the program. For example, to run *mpl.py*
 
     $ cd SourceCode
     $ python mpl.py


//add gif file


# Problem Analysis
This project aims to retrieve not only user-level, but also system-level information of pro-grams,  and  then  using  them  to  compare  two  algorithms  under  three  different  runningconditions:
   - The first program only
   - The second program only
   - The two programs at the same time


In this project, we focus on these following aspects.
   - Running time of the program
   - CPU usage
   - Memory usage (Resident set size, Virtual memory size,...)
   - Hard drive usage
   - Number of page faults

# Solution Design
First of all, we implement two programs for Predictive analysis in time series. Concretely, the first program name ***LSTM*** uses LSTM networks and the other named ***MPL*** adopts MPL networks to predict the temperature of computers. The data is collected from HPCC dataset. We run and take measurements for these programs.  In order to measure system-levelinformation, we make use of package psutil to carry out the results.  All the programs arewritten in python and were run on MacOS.

# Experimental Results
## Results

### Run each program separately 


### Run the two programs simultaneously

## Some noticeable comparisons

// add chart

# Conclusions
