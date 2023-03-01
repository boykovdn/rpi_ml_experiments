### This is the environment setup for the Raspberry Pi

## Update the system
#sudo apt update
#sudo apt upgrade

## Personal choice of editor
# sudo apt install vim

## AI requirements
pip install torch torchvision torchaudio opencv-python numpy --upgrade

## OFM Python programming client
pip install openflexure-microscope-client

## Convenience
pip install tqdm

## Debugging / displaying results
pip install matplotlib pandas

## Install Docker
#touch docker_install_script.sh
#curl -sSL https://get.docker.com > ./docker_install_script.sh
# Ideally check that the script is OK.
#sh docker_install_script.sh
#sudo usermod -aG docker $(whoami)
## Reboot the Pi, then Docker should be working.
