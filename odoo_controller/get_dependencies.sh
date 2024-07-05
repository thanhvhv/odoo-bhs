#!/bin/bash
PATH_ODOO_CONTROLLER=/home/thanhvhv/project/odoo-bhs/odoo_controller
ENTRYPOINT_SAMPLE="entrypoint.sh"
APP=$1
ADDONS=addons/$APP
ENTRYPOINT="entrypoint_$APP.sh"

cd $PATH_ODOO_CONTROLLER
# Define the file paths
cat $ENTRYPOINT_SAMPLE > $ENTRYPOINT
chmod +x $ENTRYPOINT

# touch dependencies_text
for module in `ls $ADDONS`; do 
    echo $module
    cp extract.py $ADDONS/$module
    cd $ADDONS/$module
    sed "/^#/d" __manifest__.py > copy_manifest
    python3 extract.py >> $PATH_ODOO_CONTROLLER/dependencies_text
    rm copy_manifest
    cd $PATH_ODOO_CONTROLLER
    rm $ADDONS/$module/extract.py
done

awk '!seen[$0]++' dependencies_text > dependencies_clean_text


while IFS= read -r line; do
    sed -i "33i $line" $ENTRYPOINT 
    echo $line
done < dependencies_clean_text

rm dependencies_text
rm dependencies_clean_text
