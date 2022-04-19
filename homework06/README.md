# Deploying Flask and Redis in Kubernetes

## Description of Project:
The objective of this project is to deploy the Flask application from homework 05 to the Kubernetes cloud - to create a "test" environment for our Flask application. In addition to the files from homework 05, the new files include .yml files through which k8s objects are created.

## Instructions on Running Application on Kubernetes:
Log onto isp02 through this command:
`ssh <username>@isp02.tacc.utexas.edu`

Thereafter, log onto a Kubernetes cluster through this command:
`ssh <username>@coe332-k8s.tacc.cloud

Clone the respective git repository and acquire files from coe332/homework05. 

Start all .yml files through this command:
`kubectl apply -f <filename>.yml`
- Note: You must do it for each individual file.

To ensure everything is running and to check for IDs, use this command:
`kubectl get all -o wide`

Find the IP address of your Flask service through:
```
kubectl get services
NAME                          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
kasonjim-test-flask-service   ClusterIP   10.106.43.168   <none>        5000/TCP   4h39m
```
- The IP address should be under "CLUSTER-IP". Keep note of this address.

Now exec into a Python debug container. First, you must create a .yml file containing the following:
```
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: py-debug-deployment
  labels:
    app: py-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: py-app
  template:
    metadata:
      labels:
        app: py-app
    spec:
      containers:
        - name: py39
          image: python:3.9
          command: ['sleep', '999999999']
```
Then run these commands:
`kubectl apply -f <python-debug-file-name>.yml`
`kubectl exec -it <python-debug-ID> /bin/bash`
- You can look up the python-debug-ID by this command (check under "NAME"):
```
kubectl get pods
NAME                                        READY   STATUS             RESTARTS       AGE
...
py-debug-deployment-5dfcf7bdd9-k7hxw        1/1     Running            0              3h20m
```

## Curl Requests to Server:
Once you exec into the debug deployment pod, you may now curl to the server through the Flask service IP address we took note of earlier:
```
curl -X POST 10.106.43.168:5000/data
curl 10.106.43.168:5000/data
[
 {
  "name": "Gerald",
  "id": "10001",
  "recclass": "H4",
  "mass (g)": "5754",
  "reclat": "-75.6691",
  "reclong": "60.6936",
  "GeoLocation": "(-75.6691, 60.6936)"
 },
 {
  "name": "Dominique",
  "id": "10002",
  "recclass": "L6",
  "mass (g)": "1701",
  "reclat": "-9.4378",
  "reclong": "49.5751",
  "GeoLocation": "(-9.4378, 49.5751)"
 },
 {
  "name": "Malinda",
  "id": "10003",
  "recclass": "CI1",
  "mass (g)": "3482",
  "reclat": "35.3692",
  "reclong": "61.4206",
  "GeoLocation": "(35.3692, 61.4206)"
 },

```
- The first command loads in the data.
- The second command reads the data. 
The data includes a person's name, presumably one who's analyzed the landing, its ID, class, mass of the meteorite in grams, and geolocation in latitude and longitude.
