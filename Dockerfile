FROM ubuntu:18.04
LABEL description="gui_tool"
SHELL ["/bin/bash", "-c"]
WORKDIR /gui_tool


# 1. Install basic requirements
RUN apt-get update                          &&  \
    apt-get upgrade -y                      &&  \
    apt-get install -y  git                     \
                        python3-pip             \
                        sudo                    \
                        iproute2


# 2. Install gui_tool requirements
RUN sudo apt-get install -y python3-pip python3-setuptools python3-wheel                &&  \
    sudo apt-get install -y python3-numpy python3-pyqt5 python3-pyqt5.qtsvg git-core
# Duruing installation we would run into a problem with installing PyQt5-5.15.4
# One optional is to update pip to the latest, another one is to use 5.14.0 instead.
RUN pip3 install --upgrade pip


# 3. Install the package
RUN pip3 install screeninfo
RUN git clone https://github.com/PonomarevDA/inno_uavcan_VTOL_interface --recursive --branch docker_example .
RUN pip3 install .

CMD echo "main process has been started"                        &&  \
    cd uavcan_gui_tool                                          &&  \
    uavcan_gui_tool                                             &&  \
    echo "container has been finished"
