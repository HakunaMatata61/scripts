#!/usr/bin/python3

# import using modules
import os
import time

DB_HOST = 'localhost'
DB_USER = 'admin'
DB_PASS = '1234'
DB_NAME = 'mydb'

BACKUP_DIR = '/home/dba/db/backup'
date_format = '%Y-%m-%d_%H-%M-%S'

BACKUP_INTERVAL = 20

while True:
    current_time = time.strftime(date_format)
    backup_file = f'{DB_NAME}-{current_time}.sql'
    backup_file_path = os.path.join(BACKUP_DIR, backup_file)
    mysqldump_cmd = f'mysqldump -h {DB_HOST} -u {DB_USER} -p{DB_PASS} {DB_NAME} > {backup_file_path}'
    os.system(mysqldump_cmd)
    gzip_cmd = f'gzip {backup_file_path}'
    os.system(gzip_cmd)
    find_cmd = f'find {BACKUP_DIR} -type f -name "*.gz" -mtime +7 -delete'
    os.system(find_cmd)

    time.sleep(BACKUP_INTERVAL)
