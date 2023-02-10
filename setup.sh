#!/usr/bin/sh

# In shell
# Change the user to postgres and enter password at the prompt
su - postgres

# Create postgres user and database
createuser fastapi
createdb stocks

# Access the psql shell as postgres user
psql 

# Provide the privileges to the fastapi user
alter user fastapi with encrypted password 'fastapisecret';
grant all privileges on database stocks to fastapi;

# Exit psql shell
\q

# In shell
sudo nano /etc/postgresql/15/main/pg_hba.conf

# TYPE  DATABASE    USER        ADDRESS          METHOD
local   stocks      fastapi                     md5

# Restart PostgreSQL server:
sudo service postgresql restart

psql -U fastapi stocks






