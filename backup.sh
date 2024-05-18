#!/usr/bin/env bash
# bassh script to backup and compress databases

day=$(date +"%d")
month=$(date +"%m")
year=$(date +"%Y")
file_name="$day-$month-$year.tar.gz"
#dump all databases to backup.sql
mysqldump --all-databases -u root --password="$1" > backup.sql
#compress the dumped data
tar -czvf "$file_name" backup.sql