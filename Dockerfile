FROM ubuntu:22.04

RUN apt-get update \
    && apt-get install -y \
        python3  \
        python3-pip \
        build-essential \
        wget \
        git \
    && rm -rf /var/lib/apt/lists/*

ARG CONDA_PATH=/opt/minconda3
ARG REPO_PATH=/home/flight-stack/

RUN mkdir -p $CONDA_PATH  \ 
    && wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O $CONDA_PATH/miniconda.sh \ 
    && bash $CONDA_PATH/miniconda.sh -b -u -p $CONDA_PATH \
        rm -rf $CONDA_PATH/miniconda.sh


ENV PATH="$CONDA_PATH/bin:${PATH}"

RUN conda env create -f $REPO_PATH/quad-simulation/quad-sim-env.yml

USER flight-stack
WORKDIR $REPO_PATH

CMD ["bash"]
