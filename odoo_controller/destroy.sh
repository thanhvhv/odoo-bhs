#!/bin/bash
PATH_ODOO_CONTROLLER=/home/thanhvhv/project/myodoo/odoo_controller
APP=$1

cd $PATH_ODOO_CONTROLLER
# Define the name of app
docker compose -p $APP down -v
rm -r ./addons/$APP
rm entrypoint_$APP.sh
sed -i "/$APP/d" ./port_data.txt