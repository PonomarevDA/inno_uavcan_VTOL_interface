#!/bin/bash

cd "$(dirname "$0")"
source config.sh

FLAGS_FOR_DEV=""
if [ "$DEV_NAME" = "slcan" ]; then
    FLAGS_FOR_DEV="--net=host"
elif [ -z "$DEV_NAME"] ; then
    echo "DEV_NAME is not set. Exit."
    exit
else
    FLAGS_FOR_DEV="--privileged -v $DEV_NAME:$DEV_NAME"

fi
FLAGS_FOR_DUSPLAYING_GUI="-v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY"


xhost +local:docker
echo running $REPOSITORY_NAME:$TAG_NAME $FLAGS_FOR_DEV
sudo docker container run --rm                  \
    $FLAGS_FOR_DEV                              \
    $FLAGS_FOR_DUSPLAYING_GUI                   \
    $REPOSITORY_NAME:$TAG_NAME
