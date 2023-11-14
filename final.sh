#!/bin/env bash

LOCAL_DIR="./bd-al/service-result"
mkdir -p $LOCAL_DIR

CONTAINER_NAME="assignment"
docker cp $CONTAINER_NAME:/home/doc-bd-a1/res_dpre.csv $LOCAL_DIR
docker cp $CONTAINER_NAME:/home/doc-bd-a1/eda-in-1.txt $LOCAL_DIR
docker cp $CONTAINER_NAME:/home/doc-bd-a1/vis.png $LOCAL_DIR
docker cp $CONTAINER_NAME:/home/doc-bd-a1/k.txt $LOCAL_DIR
docker stop $CONTAINER_NAME
