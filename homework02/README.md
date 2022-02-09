Robotic Vehicle on Mars

The project's objective is to simulate a robotic vehicle on Mars investigating five meteorite landing sites. The folder contains two python scripts and a json file (generated from the first python script) that obtains the objective. 

The first python script generates sites by creating a dictionary with a "sites" key that contains a lists of dictionaries - in each dictionary holds data about the specific sites that contain information that were randomly generated. Thereafter, the script saves the data to a JSON file in order to startthe next python script.

The second python script reads in the meteorite site JSON file and calculates the time required to visit each site and take its samples. It utilizes mathematical functions and conditional statements and loops to iterate through the JSON file, gathering information about distances and time. 

   
