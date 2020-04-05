#! /bin/bash

# Start the Data Import Daemon
# python data_import_daemon.py &

# Migrate Database
flask db upgrade 

# Run!
flask run -h "${APP_HOST}" -p "${APP_PORT}"
