FROM ubuntu

## Update the system
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install git vim python-is-python3 python3-pip -y
RUN echo "pip version: $(pip3 --version)"

## Debugging / displaying results
RUN pip install matplotlib pandas tqdm imageio numpy --upgrade

## The OFM client
RUN pip install openflexure_microscope_client
