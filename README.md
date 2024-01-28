# flight-stack

Flight Stack is a learning environment for quadcopters 

The philosophy is to be easy to use, very simple documentation is in this README, else all other detailed info can be found here:
https://flightstack.wordpress.com/

## Dev Environment

Build the docker environment

```bash
docker build . -t flight-stack-dev-env
```

```bash
conda activate quad-sim-env
```

## Build Instructions

```bash
docker run -it --rm flight-stack-dev-env:latest
```

## Flash Instructions


