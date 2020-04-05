import os, datetime, time

def log(message):
    filename = '/var/log/data_importer.log'
    file = open(filename, 'a')
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file.write(str.format('{} - {}\n', timestamp, message))
    file.close()

def importData():
    while 1:
        log('Importing Data...')

        log('Sleeping for 5 seconds.')
        time.sleep(5)

if __name__ == '__main__':
    log('Starting Data Import Daemon')
    importData()
else:
    log('Data Import Daemon not started.')
