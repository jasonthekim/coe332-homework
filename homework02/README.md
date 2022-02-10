Robotic Vehicle on Mars

The project's objective is to simulate a robotic vehicle on Mars investigating five meteorite landing sites. The folder contains two python scripts and a json file (generated from the first python script) that obtains the objective. 

The first python script, generate_sites.py, generates sites by creating a dictionary with a "sites" key that contains a lists of dictionaries - in each dictionary holds data about the specific sites that contain information that were randomly generated. Thereafter, the script saves the data to a JSON file in order to start the next python script.

The second python script, calculate_trip.py, reads in the meteorite site JSON file and calculates the time required to visit each site and to take its samples. It utilizes mathematical functions and conditional statements/loops to iterate through the JSON file, gathering information about distances and time. 

As for running the code, the user must first run generate_sites.py to generate the JSON file so that calculate_trip.py can read the JSON file and print the results. Through linux, to run the python scripts, you must type 'python3 <file>'. The results show each leg with its time travel and the time it took to sample the composition; the number of legs; and total time elapsed (time to travel + time to sample).  
