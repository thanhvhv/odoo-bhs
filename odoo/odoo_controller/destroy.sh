#!/bin/bash
PATH_ODOO_CONTROLLER=./odoo/odoo_controller
APP=$1

cd $PATH_ODOO_CONTROLLER
# Define the name of app
docker exec -i "$APP"_odoo_1 chown -R 1000:1000 /mnt/extra-addons/
docker exec -i "$APP"_odoo_1 chown 1000:1000 /entrypoint.sh 

docker compose -p $APP down -v
rm -r ./addons/$APP
rm entrypoint_$APP.sh
sed -i "/$APP/d" ./port_data.txt
