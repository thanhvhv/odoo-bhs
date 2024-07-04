#!/bin/bash 
# Execute the command
nc -zv 127.0.0.1 8000
# Get the exit code of the command
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    # port not available
    echo "123"
elif [ $CHECK_APP_EXIST ]; then
    # app available
    # ODOO_APP=$APP VERSION_ODOO=$VERSION_ODOO ODOO_PORT=$PORT docker-compose -p $APP up -d
    echo "456"  
else
    # ODOO_APP=$APP VERSION_ODOO=$VERSION_ODOO ODOO_PORT=$PORT docker-compose -p $APP up -d
    echo "789"  
fi
