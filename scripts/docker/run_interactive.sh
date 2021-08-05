#!/bin/bash

cd "$(dirname "$0")"
source config.sh

xhost +local:docker
echo running $REPOSITORY_NAME:$TAG_NAME
sudo docker container run --rm -it              \
    --privileged -v /dev/bus/usb:/dev/bus/usb   \
    -v /tmp/.X11-unix:/tmp/.X11-unix            \
    -e DISPLAY=$DISPLAY                         \
    $REPOSITORY_NAME:$TAG_NAME /bin/bash
