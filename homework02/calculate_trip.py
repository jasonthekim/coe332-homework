import json
import math

# get json file from part 1
with open('sites.json', 'r') as f:
    sites_data = json.load(f)

# initial conditions
mars_radius = 3389.5    
max_robot_speed = 10
lat0 = 16.0
lon0 = 82.0
totalt = 0.0

# great-circle algorithm to calculate dist between points
def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

# for loop to iterate through 'sites' key with a list of dictionaries
for i in range(len(sites_data['sites'])):
   
    stony_time = 1
    iron_time = 2
    stony_iron_time = 3    
    t0 = 0.0
    t = 0.0

    print('leg =', i+1),

# two if statements to account for previous/initial site; calculates time it takes to travel from one site to another using calc_gcd function   
    if i == 0:
        t0 = calc_gcd( lat0, lon0, sites_data['sites'][i]['latitude'], sites_data['sites'][i]['longitude'] ) / max_robot_speed
        print('time to travel =', '{:.2f}'.format(t0), 'hr')
   
    if i != 0:
        t = calc_gcd( sites_data['sites'][i-1]['latitude'], sites_data['sites'][i-1]['longitude'], sites_data['sites'][i]['latitude'], sites_data['sites'][i]['longitude'] ) / max_robot_speed
        print('time to travel =', '{:.2f}'.format(t), 'hr')   

# if-else statements to check type of composition and assign appropriate time to sample to current_samplet
    if sites_data['sites'][i]['composition'] == 'stony':
        current_samplet = stony_time 
        print('time to sample =', '{:.2f}'.format(stony_time, 'hr'))
    elif sites_data['sites'][i]['composition'] == 'iron':
        current_samplet = iron_time
        print('time to sample =', '{:.2f}'.format(iron_time), 'hr')
    else:
        current_samplet = stony_iron_time
        print('time to sample =', '{:.2f}'.format(stony_iron_time), 'hr')

# update totalt after iteration    
    totalt = totalt + t0 + t + current_samplet

# print new line for aesthetic purposes 
    print()

#display total number of legs and total time elapsed
print('number of legs =', len(sites_data['sites']))
print('total time elapsed =', '{:.2f}'.format(totalt), 'hr')
