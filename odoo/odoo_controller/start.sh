#!/bin/bash
PATH_ODOO_CONTROLLER=./odoo/odoo_controller
APP=$1

cd $PATH_ODOO_CONTROLLER
# Define the name of app
docker compose -p $APP start
