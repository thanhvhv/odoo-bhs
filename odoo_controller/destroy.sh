#!/bin/bash
PATH_ODOO_CONTROLLER=/home/thanhvhv/project/myodoo/odoo-bhs/odoo_controller
APP=$1

cd $PATH_ODOO_CONTROLLER
# Define the name of app
docker exec -i $APP chown -R 1000:1000 /mnt/extra-addons/
docker compose -p $APP down -v
rm -r ./addons/$APP
rm entrypoint_$APP.sh
sed -i "/$APP/d" ./port_data.txt