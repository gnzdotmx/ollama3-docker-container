# Run ollama3

## Download the repository and setup llama3 docker
Download this repository to your computer
```
git clone https://github.com/gnzdotmx/ollama3-docker-container.git
```

Download and run the docker container to setup ollama
```
$ cd docker
$ docker compose up -d ollama
```

Download the llama3 model by running the following command. Once the prompt starts, execute `/exit`
```
$ docker exec -it ollama ollama run llama3
```


## Create a python environment

Create a python environment called `llama3`
```
$ python3 -m venv llama3
```

Activate the environment
```
$ source llama3/bin/activate
```

Run the python script to start chatting with ollama3
```
$ python base_lm3.py
```
