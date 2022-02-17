 **Mars Lab Water Safety**
 
The project's objective is to check whether the latest water quality data from the five meteorite samples is safe to use. The folder contains two pytho    n scripts, one of which calculates the turbidity of water and the other calculating the minimum time required to reach below the safety threshold, in o    rder to obtain the objective.
  
In order to download the data set from the original source, you can download [this link](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json) and copy/paste the data in a JSON file. An alternative way is to type this in the command line:

    wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json

this command autoamtically creates a JSON file called turbidity_data.json containing the data.

The first python script, analyze_data.py, calculates the average turbidity based on the most recent five measurements from the turbidity data set; dete    rmines whether the turbidity value is above or below the safety threshold; and lastly calculates the minimum time required to return below a safe thres    hold. The script implements two functions and a main to print the results by calling the functions.

The second python script, test_analyze_data.py, imports pytest to run tests on the two functions, calculate_turbidity and minimum_time_threshold, from the first python script. It performs simple sanity checks that the math is correct, checks types returned and exceptions thrown what are expected.

As for running the code, it is important to have created a JSON file containing the turbidity data set before running the first python script, analyze_turbidity.py so that it can import and read the JSON data. Thereafter, are we able to run the test script to make sure the functions work properly.  


