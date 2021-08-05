#!/bin/bash
cd "$(dirname "$0")"
source config.sh

sudo docker build -t $REPOSITORY_NAME:$TAG_NAME $DOCKERFILE_RELATIVE_PATH
