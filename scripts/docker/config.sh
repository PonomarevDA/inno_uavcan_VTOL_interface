#!/bin/bash

TAG_NAME=v0.2.3
if uname -m | grep -q 'aarch64'; then
   TAG_NAME="$TAG_NAME""arm64"
elif uname -m | grep -q 'x86_64'; then
   TAG_NAME="$TAG_NAME""amd64"
else
    echo "unknown architecture"
    exit
fi
REPOSITORY_NAME=gui_tool
DOCKERFILE_RELATIVE_PATH=../..