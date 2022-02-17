import json
import math 
import logging


# with open('turbidity_data.json', 'r') as f:
   # turb_data = json.load(f)

# turbidity threshold for safe water
Ts = 1.0

# function to calculate average turbidity
def calculate_turbidity(listOfDicts, keyString, keyString2):
    """calculates average turbidity of water.

    Iterates through x amount of dicts in listOfDicts, capturing two values needed to calculate turbidity of water in each dict, and finds the average of x amount of turbidity values.. 

    Args: 
        listOfDicts: a list of dictionaries, each dict containing same set of keys.
        keyString: a key with string type inside listOfDicts (in hw's case, either the calibration constant or ninety degree detector current).
        keyString2: a key with string type inside listOfDicts (in hw's case, either the calibration constant or ninety degree detector current).

    Returns:
        A float value that represents the average turbidity of water across x amount of dictionaries. 

    Raises:
        KeyError: keyString and/or keyString2 not in dictionary of listOfDicts.
        KeyError: not enough keys in dictionaries (must require at least two).                 
   
    """
    Ttotal = 0.0

    for item in listOfDicts[-5:]:
        T = item[keyString] * item[keyString2]
        Ttotal += T     

    return( Ttotal / len(listOfDicts[-5:]) )

# function to calculate time to go below threshold
def minimum_time_threshold(currentTurb, decayFactor, threshold):
    """calculates minimum time required to reach below threshold
    
    Checks whether current turbidity is greater than safe threshold. if so, finds minimum time to get below threshold by using given decay factor constant and math inequality. otherwise, return 0 hours. 

    Args:
        currentTurb: float value retrieved from calculate_turbidity function.
        decayFactor: constant float value given from problem, respresenting the decay factor per hour of turbidity.
        threshold: constant float value given from problem, representing safe threshold value. 

    Returns:
        A float value that represents the minimum time, in hours, required to reach below safe threshold value.

    Raises: 
        TypeError: value not a float (cannot take strings etc.).
        ZeroDivisionError: decay factor is zero which leads to dividing by zero, which is unallowed.

    """   
    # T0 = calculate_turbidity(turb_data['turbidity_data'], 'calibration_constant', 'detector_current')
    
    if currentTurb > threshold:
        tmin = -math.log(currentTurb) / math.log(1 - decayFactor)
        tminf = '{:.2f}'.format(tmin)
        return float(tminf)
    else:
        return 0  


# main function 
def main():

    with open('turbidity_data.json', 'r') as f:
        turb_data = json.load(f)

# print average turbidity
    T = calculate_turbidity(turb_data['turbidity_data'], 'calibration_constant', 'detector_current')
    print('Average turbidity based on most recent five measurements =', '{:.4f}'.format(T),'NTU' )
    
# check if above threshold
    logging.basicConfig(level = logging.INFO, format = f'%(message)s')

    if T < Ts:
        logging.info('Info: Turbidity is below threshold for safe use')
    else:
        logging.warning('Warning: Turbidity is above threshold for safe use')
    
# print min time required to return below safe threshold, if turbidity above 1.0
    d = 0.02
    tmin = minimum_time_threshold(T, d, Ts)      
    print( 'Minimum time required to return below a safe threshold =', tmin, 'hours' )

if __name__ == '__main__':
    main()
