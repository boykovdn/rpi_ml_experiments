FROM ubuntu

## Update the system
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install git vim python-is-python3 python3-pip -y
RUN echo "pip version: $(pip3 --version)"

## AI requirements
RUN pip install torch torchvision torchaudio opencv-python numpy --upgrade
## Debugging / displaying results
RUN pip install matplotlib pandas tqdm imageio
## Extra libs for Cellpose
RUN pip install scipy opencv-python-headless tifffile numba fastremap natsort

## Getting access to the cellpose model and avoiding a full installation.
## This is done by cloning the CP repo and adding a symlink to the python
## path. I expect some features of CP to break, but we only need to be able
## to run the neural network headlessly from our scripts, hence need to be
## able to import the models.py module.
ENV CP_REPO_PATH=/root/cellpose
ENV CP_PATH=${CP_REPO_PATH}/cellpose
RUN git clone https://github.com/MouseLand/cellpose $CP_REPO_PATH
RUN ln -s $CP_PATH /usr/lib/python3/dist-packages
## Initialize the CP model so that the weights are downloaded locally.
RUN python -c "from cellpose.models import Cellpose; cp = Cellpose()"

RUN mkdir /data
