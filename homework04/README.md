# Containerizing Meteorite Landing Data Analysis

## _Folder contents and project objective_

The project's objective is to modify the ml_data_analysis.py script to take the name of the JSON file as a command line argument and in its output to print in a more organized and readable manner and containerize important scripts and files in order to release the application to the world. The folder contains two python scripts, a meteorite landings json file, and a Dockerfile, an important file that allows for containerization. 

## _Description of the main files_
ml_data_analysis.py:
- calculates average mass of meteors in dataset.
- checks which hemisphere quadrant each meteor's in, keeping count of how many are in each quadrant.
- determines which class meteor is in, keeping count of how many are in each class.
- outputs all such info in an organized manner.

test_ml_data_analysis.py:
- makes sure each function in ml_data_analysis.py has no errors.
- has a minimum of five tests for each of the three functions.
- tests check that input parameters are correct and math is correct.

Dockerfile:
- containerizes meteorite landings dataset, analysis script, and test script.
- is pushed to dockerhub where people around the world can access it

## _How to run code in order_

1. Pull and use existing image on Docker Hub by typing in command line:
   - docker pull jasonthekim/ml_data_analysis:hw04

2. Build an image from my Dockerfile by typing in command line:
   - docker build -t <username>/ml_data_analysis:<version> .

3. Run the containerized code against the sample data inside the container by typing in command line(the first line gets user into container; second runs the code against the data):
   - docker run --rm -it <username>/ml_data_analysis:<version> /bin/bash
   - ml_data_analysis /code/Meteorite_Landings.json

Expected output:
    Average mass of 30 meteor(s):
    83857.3 grams

    Hemisphere summary data:
    There were 21 meteors found in the Northern & Eastern quadrant
    There were 6 meteors found in the Northern & Western quadrant
    There were 0 meteors found in the Southern & Eastern quadrant
    There were 3 meteors found in the Southern & Western quadrant

    Class summary data:
    The L5 class was found 1 times
    The H6 class was found 1 times
    The EH4 class was found 2 times
    The Acapulcoite class was found 1 times
    The L6 class was found 6 times

    ... etc

In interpreting the output, the output shows the average mass of all 30 meteors in the dataset, the amount of meteors in each hemisphere, and lastly the amount of meteors found in each class.

4. Run the containerized code against the user-provided data:
   - docker run --rm -it -v $PWD:/data username/ml_data_analysis:1.0 /bin/bash
   - ml_data_analysis.py /data/<user-provided data file name>

5. Run the containerized test suite with pytest:
   - docker run --rm <username>/ml_data_analysis:<version> pytest /code/

Expected output:
    ============================= test session starts ==============================
    platform linux -- Python 3.6.8, pytest-7.0.0, pluggy-1.0.0
    rootdir: /code
    collected 3 items

    code/test_ml_data_analysis.py ...                                        [100%]

    ============================== 3 passed in 0.06s ===============================

In interpreting the pytest output, the fourth line shows how many function tests were collected, the line after shows which test script it tested, and the last line ultimately shows whether all tests passed. 
    
## _Expected input data_
It is important to note that the input data should cater to the ml_data_analysis.py script. The input data should have a list of dictionaries, with each dict containing same set of key(s). 

Example of proper input data:
    {
      "meteorite_landings": [
        {
          "name": "Ruiz",
          "id": "10001",
          "recclass": "L5",
          "mass (g)": "21",
          "reclat": "50.775",
          "reclong": "6.08333",
          "GeoLocation": "(50.775, 6.08333)"
        },
        {
          "name": "Beeler",
          "id": "10002",
          "recclass": "H6",
          "mass (g)": "720",
          "reclat": "56.18333",
          "reclong": "10.23333",
          "GeoLocation": "(56.18333, 10.23333)"
        },
        {
          "name": "Brock",
          "id": "10003",
          "recclass": "EH4",
          "mass (g)": "107000",
          "reclat": "54.21667",
          "reclong": "-113",
          "GeoLocation": "(54.21667, -113.0)"
        },
    etc...

To analyze a different set of Meteorite Landings data:
1. Download the data by either clicking [this link](https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json) and copy/paste into a json file, or typing this into the command line:
    wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json 

2. Because we didn't copy this JSON file into the container at build time and run time, in order to run the containerized scripts against this specific dataset, you must mount the data inside the container:
    docker run --rm -it -v $PWD:/data <username>/ml_data_analysis:<version> /bin/bash 
    ml_data_analysis.py /data/<data_set_name.json>




