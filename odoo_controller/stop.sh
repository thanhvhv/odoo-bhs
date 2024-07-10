#!/bin/bash
PATH_ODOO_CONTROLLER=/home/thanhvhv/project/myodoo/odoo-bhs/odoo_controller
APP=$1

cd $PATH_ODOO_CONTROLLER
# Define the name of app
docker compose -p $APP stop