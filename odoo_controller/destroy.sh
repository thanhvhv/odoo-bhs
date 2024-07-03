#!/bin/bash

APP=$1

# Define the name of app
docker compose -p $APP down -v
rm -r ./addons/$APP
rm entrypoint_$APP.sh
sed -i "/$APP/d" ./port_data.txt