#!/bin/bash
WORK_SPACE=/home/thanhvhv/project/odoo-bhs
PATH_ODOO_CONTROLLER=/home/thanhvhv/project/myodoo/odoo-bhs/odoo_controller


# Define the name of app
APP=$1

# Define the port number to check
PORT=$2

VERSION_ODOO=$3
shift 3;

cd $PATH_ODOO_CONTROLLER/addons
mkdir $APP

cd $WORK_SPACE

for param in "$@"; do
    cp -r $WORK_SPACE/odoo_module/O_$VERSION_ODOO/$param $PATH_ODOO_CONTROLLER/addons/$APP
done

cd $PATH_ODOO_CONTROLLER
./get_dependencies.sh $APP
ls

# Execute the command
nc -zv 127.0.0.1 $PORT
# Get the exit code of the command
EXIT_CODE=$?
CHECK_APP_EXIST=`grep "$APP" port_data.txt | cut -d ':' -f 2`
CHECK_PORT_EXIST=`grep "$PORT" port_data.txt | cut -d ':' -f 2`

if [ $EXIT_CODE -eq 0 ]; then
    # port not available
    ./destroy.sh $CHECK_PORT_EXIST
    ODOO_APP=$APP VERSION_ODOO=$VERSION_ODOO ODOO_PORT=$PORT docker-compose -p $APP up -d
    echo "123"
    echo "$PORT:$APP" >> ./port_data.txt
elif [ $CHECK_APP_EXIST ]; then
    # app available
    ./destroy.sh $CHECK_APP_EXIST
    ODOO_APP=$APP VERSION_ODOO=$VERSION_ODOO ODOO_PORT=$PORT docker-compose -p $APP up -d
    echo "456"
    echo "$PORT:$APP" >> ./port_data.txt  
else
    ODOO_APP=$APP VERSION_ODOO=$VERSION_ODOO ODOO_PORT=$PORT docker-compose -p $APP up -d
    echo "789"
    echo "$PORT:$APP" >> ./port_data.txt  
fi