# The Million Dollar Diagram

This assignment entails a software diagram that illustrates the API - which navigates through the ISS Sighting Data, returning desired information - of our midterm project. It shows the various routes the user can call to return specific information about the respective data. 

1. The first step, illustrated by the blue oval, is to start running the flask app, which can be done by running the following commands:
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run -p 5000
```

2. The second step, illustrated by the orange square, entails reading/loading in the data, which can be done by running the command: `curl localhost:5000/read_data -X POST`

3. After loading in the data, the user may go down the left path - the orange rectangle with "/help" - to see what each route does, which can be done through the following command: `curl localhost:5000/help`

4. Assuming that the user knows the name and what each route does, he/she can move onto the right side of the diagram, which allows the user to return information about a specific epoch or information about a country, its region, and city. 
- Note, on the right side of the diagram, the purple boxes return a specific entity within the prior orange box. 
- Furthemore, the orange boxes list all the epochs or countries, and the purple boxes return specific info about the desired country/region/city.

### Citation (Link to Midterm Project)
You may access the Midterm Project through [this link](https://github.com/jasonthekim/SimplificationOfISS) 
