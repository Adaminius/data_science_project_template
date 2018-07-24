#!/usr/bin/env bash
#A template for writing bash scripts using variables contained in .env

#Check if .env exists before running script: 
if [ ! -f .env ]; then
    echo "No .env file found"
    exit 1
fi

set -a
[ -f .env ] && . .env
set +a

#Check if the variables you need are defined before running script:
if [ -z ${PROJ_BASE} ]; then
    echo "requires a .env file containing 'PROJ_BASE=...'"
    exit 1
fi

echo "This project's root directory is at ${PROJ_BASE}"  
