# **Mars Lab Water Safety**
 
## *Section 1: Folder contents and project objective*

The project's objective is to check whether the latest water quality data from the five meteorite samples is safe to use. The folder contains two pytho    n scripts, one of which calculates the turbidity of water and the other calculating the minimum time required to reach below the safety threshold, in o    rder to obtain the objective.

## *Section 2: How to download the data set*  

In order to download the data set from the original source, you can download [this link](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json) and copy/paste the data in a JSON file. An alternative way is to type this in the command line:

    wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json

this command automatically creates a JSON file called turbidity_data.json containing the data.

## *Section 3: Description of python scripts*

The first python script, analyze_data.py, calculates the average turbidity based on the most recent five measurements from the turbidity data set; dete    rmines whether the turbidity value is above or below the safety threshold; and lastly calculates the minimum time required to return below a safe thres    hold. The script implements two functions and a main to print the results by calling the functions.

The second python script, test_analyze_data.py, imports pytest to run tests on the two functions, calculate_turbidity and minimum_time_threshold, from the first python script. It performs simple sanity checks that the math is correct, checks types returned and exceptions thrown what are expected.

## *Section 4: How to run code in order and how to interpret results*

As for running the code, it is important to have created a JSON file containing the turbidity data set before running the first python script, analyze_turbidity.py so that it can import and read the JSON data. Thereafter, are we able to run the test script to make sure the functions work properly. In interpreting the results, the analyze_turbidity.py script will output similar to one of the following two code blocks:
   
    Average turbidity based on most recent five measurements = 1.1992 NTU
    Warning: Turbidity is above threshold for safe use
    Minimum time required to return below a safe threshold = 8.99 hours 	  

    Average turbidity based on most recent five measurements = 0.9852 NTU
    Info: Turbidity is below threshold for safe use
    Minimum time required to return below a safe threshold = 0 hours

where it shows the average turbidity (in NTU units & rounded to four decimal places), a warning or info message stating whether the water is safe, and the minimum time required to return below a safe threshold, respectively. 

