# Flask Store API

## Install
```
pip3 install -r requirements.txt
python3 app.py
```

## Run in a docker container
```
1. docker build -t items:v1 .
2. docker run -d --name items-api -p 5000:5000 items:v1
```