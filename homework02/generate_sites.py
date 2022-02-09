import random
import json

latitude_list = []
longitude_list = []

meteorite_comp = ['stony', 'iron', 'stony-iron']

sites_dict = {"sites": [ {"site_id": 1, "latitude": random.uniform(16.0,18.0), "longitude": random.uniform(82.0,84.0), "composition": random.choice(meteorite_comp)}, 
{"site_id": 2, "latitude": random.uniform(16.0,18.0), "longitude": random.uniform(82.0,84.0), "composition": random.choice(meteorite_comp)},
{"site_id": 3, "latitude": random.uniform(16.0,18.0), "longitude": random.uniform(82.0,84.0), "composition": random.choice(meteorite_comp)},
{"site_id": 4, "latitude": random.uniform(16.0,18.0), "longitude": random.uniform(82.0,84.0), "composition": random.choice(meteorite_comp)},
{"site_id": 5, "latitude": random.uniform(16.0,18.0), "longitude": random.uniform(82.0,84.0), "composition": random.choice(meteorite_comp)}
]

} 

with open('sites.json', 'w') as out:
    json.dump(sites_dict, out, indent=2)


for i in range(5):
    latitude_list.append(random.uniform(16.0,18.0))
    longitude_list.append(random.uniform(82.0,84.0))



\


