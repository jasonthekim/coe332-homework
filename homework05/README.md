# Combining Redis and Flask

## Instructions to Launch the Redis Database:
1. Log onto ISP server and type into the command line: `docker run -v $(pwd)/data:/data -p <flask port>:6379 -d --name <name>-redis redis:6 --save 1 1`
    - It is important to add the `-d` flag, as it allows for it start in the background (detached or daemon mode). 
    - The `-v` flag performs a bind mount which is a way of replacing a file or directory in a container image with a file or directory on the host file system in a running container.
    - The `--save 1 1` configures the data base server to save to 1 backup file every 1 second - all in order to persist the data across redis containers.


## Instructions to Pull/Build/Launch Flask App:
1. On the ISP/TACC server, to create Dockerfile, type in command line: `touch Dockerfile`
2. Specify requirements needed for Flask application by typing in command line: `vim requirements.txt`
3. In the file created in step 2 type: `Flask==2.0.3` and save.
4. Open the created Dockerfile and enter in:
```
FROM python:3.9

RUN mkdir /app
RUN pip3 install --user redis
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . /app

ENTRYPOINT ["python"]
CMD ["app.py"]
```
5. Build the container by typing in command line: `docker build -t <username>/<file-name>:<name> .`
6. Push the container by typing in command line: `docker push <username>/<file-name>:<name>`
7. To pull the pre-containerized copy of app from Docker Hub, type in command line: `docker pull <username>/<file-name>:<name>
`
8. Finally, to launch and interact with the Flask application, type and run in command line:
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run -p <flask port #>
```

## Instructions to Perform POST and GET Requests to Flask App:
1. Open a separate window terminal in linux.
2. Type in command line: `curl localhost:<flask port #>/data -X POST`
    - This command loads the Meteorite Landings data and confirms that it has been read successfully.
3. Type in command line: `curl localhost:<flask port #>/data`
    - This command reads the data out of Redis and returns it as a JSON list.

## Description of Data:
Sample of data:
```
  {
    "name": "Agnes",
    "id": "10298",
    "recclass": "H6",
    "mass (g)": "801",
    "reclat": "-61.5820",
    "reclong": "-10.3998",
    "GeoLocation": "(-61.5820, -10.3998)"
  },
  {
    "name": "Jennifer",
    "id": "10299",
    "recclass": "L5",
    "mass (g)": "539",
    "reclat": "-84.0579",
    "reclong": "69.9994",
    "GeoLocation": "(-84.0579, 69.9994)"
  },
  {
    "name": "Christina",
    "id": "10300",
    "recclass": "H5",
    "mass (g)": "4291",
    "reclat": "-38.1533",
    "reclong": "-46.7127",
    "GeoLocation": "(-38.1533, -46.7127)"
  }
 
```
The data includes a person's name, presumably one who's analyzed the landing, its ID, class, mass of the meteorite in grams, and geolocation in latitude and longitude. 

