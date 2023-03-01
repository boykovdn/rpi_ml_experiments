FROM 7a7d343029a2 

## Update the system
#RUN apt update
#RUN apt upgrade -y
#RUN apt-get install git vim python-is-python3 python3-pip -y --upgrade
#RUN echo "pip version: $(pip3 --version)"

## AI requirements
#RUN pip install torch torchvision torchaudio opencv-python numpy --upgrade
## Debugging / displaying results
#RUN pip3 install matplotlib pandas tqdm imageio

## Getting access to the cellpose model and avoiding a full installation.
## This is done by cloning the CP repo and adding a symlink to the python
## path. I expect some features of CP to break, but we only need to be able
## to run the neural network headlessly from our scripts, hence need to be
## able to import the models.py module.
ENV CP_REPO_PATH=/root/cellpose
ENV CP_PATH=${CP_REPO_PATH}/cellpose
RUN git clone https://github.com/MouseLand/cellpose $CP_REPO_PATH
# Clear the contents of __init__.py
RUN rm ${CP_PATH}/__init__.py; touch ${CP_PATH}/__init__.py
RUN ln -s $CP_PATH /usr/lib/python3/dist-packages
## Initialize the CP model so that the weights are downloaded locally.
#RUN python -c "from cellpose.models import Cellpose; cp = Cellpose()"

RUN pip3 -vv install tqdm scipy
RUN apt update || :
RUN apt install vim -y
RUN pip3 install tifffile
## Extra libs for Cellpose
#RUN pip3 install llvmlite
#RUN pip3 install numba fastremap natsort

## OFM client
RUN pip3 install openflexure_microscope_client
