FROM 7a7d343029a2 

## Update the system
#RUN wget https://apt.kitware.com/kitware-archive.sh
#RUN sh kitware-archive.sh
#RUN wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - | tee /usr/share/keyrings/kitware-archive-keyring.gpg >/dev/null \
#    && echo 'deb [signed-by=/usr/share/keyrings/kitware-archive-keyring.gpg] https://apt.kitware.com/ubuntu/ focal main' | tee /etc/apt/sources.list.d/kitware.list >/dev/null
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 42D5A192B819C5DA
RUN apt-get update
RUN apt-get upgrade -y
#RUN apt-get install gpg wget
#RUN wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - | sudo tee /usr/share/keyrings/kitware-archive-keyring.gpg >/dev/null
#RUN echo 'deb [signed-by=/usr/share/keyrings/kitware-archive-keyring.gpg] https://apt.kitware.com/ubuntu/ bionic main' | sudo tee /etc/apt/sources.list.d/kitware.list >/dev/null
#RUN apt-get update

RUN pip3 install --upgrade pip
RUN echo "pip version: $(pip3 --version)"
#RUN apt install git vim -y --upgrade

## Debugging / displaying results
#RUN pip3 install matplotlib pandas tqdm imageio

## Getting access to the cellpose model and avoiding a full installation.
## This is done by cloning the CP repo and adding a symlink to the python
## path. I expect some features of CP to break, but we only need to be able
## to run the neural network headlessly from our scripts, hence need to be
## able to import the models.py module.
#ENV CP_REPO_PATH=/root/cellpose
#ENV CP_PATH=${CP_REPO_PATH}/cellpose
#RUN git clone https://github.com/MouseLand/cellpose $CP_REPO_PATH
#RUN ln -s $CP_PATH /usr/lib/python3/dist-packages
## Initialize the CP model so that the weights are downloaded locally.
#RUN python -c "from cellpose.models import Cellpose; cp = Cellpose()"

## Installing lightseg
ENV LS_REPO_PATH=/root/lightseg
ENV LS_PATH=${LS_REPO_PATH}
RUN git clone https://github.com/rzuberi/lightseg $LS_REPO_PATH
RUN sed -i 's/[~=].*//' ${LS_REPO_PATH}/requirements.txt
RUN cat ${LS_REPO_PATH}/requirements.txt
RUN pip3 install -r ${LS_REPO_PATH}/requirements.txt
RUN ln -s $LS_PATH /usr/lib/python3/dist-packages
RUN python -c "from cellmask_model import CellMaskModel; model = CellMaskModel()"

#RUN pip3 -vv install tqdm scipy
#RUN apt update || :
#RUN apt install vim -y
#RUN pip3 install tifffile
## Extra libs for Cellpose
#RUN pip3 install llvmlite
#RUN pip3 install numba fastremap natsort
