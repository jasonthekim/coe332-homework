import json
import math 

# with open('turbidity_data.json', 'r') as f:
   # turb_data = json.load(f)

# turbidity threshold for safe water
Ts = 1.0

# function to calculate average turbidity
def calculate_turbidity(listOfDicts, keyString, keyString2):
   
    Ttotal = 0.0

    for item in listOfDicts[-5:]:
        T = item[keyString] * item[keyString2]
        Ttotal += T     

    return( Ttotal / len(listOfDicts[-5:]) )

# function to calculate time to go below threshold
def minimum_time_threshold(currentTurb, decayFactor, threshold):
   
    # T0 = calculate_turbidity(turb_data['turbidity_data'], 'calibration_constant', 'detector_current')
    
    if currentTurb > threshold:
        tmin = -math.log(currentTurb) / math.log(1 - decayFactor)
        print( 'Minimum time required to return below a safe threshold =', '{:.2f}'.format(tmin) )
    else:
        print( 'Minimum time required to return below a safe threshold = 0 hours' )  


# main function 
def main():

    with open('turbidity_data.json', 'r') as f:
        turb_data = json.load(f)

# print average turbidity
    T = calculate_turbidity(turb_data['turbidity_data'], 'calibration_constant', 'detector_current')
    print('Average turbidity based on most recent five measurements =', '{:.4f}'.format(T),'NTU' )
    
# check if above threshold
    if T < Ts:
        print( 'Info: Turbidity is below threshold for safe use' )
    else:
        print( 'Warning: Turbidity is above threshold for safe use' )     
    
# print min time required to return below safe threshold, if turbidity above 1.0
    d = 0.02
    minimum_time_threshold(T, d, Ts)      
 
    
if __name__ == '__main__':
    main()




