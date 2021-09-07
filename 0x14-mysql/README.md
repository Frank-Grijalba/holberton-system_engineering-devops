## holberton-system_engineering-devops

# General
- What is the main role of a database
- What is a database replica
- What is the purpose of a database replica
- Why database backups need to be stored in different physical locations
- What operation should you regularly perform to make sure that your database backup strategy actually works

In this exercises the command: mysql> show master status;
Show me next result:
File             | Position | Binlog_Do_DB
mysql-bin.000001 |      154 | tyrell_corp

For configuring management into slave server:

CHANGE MASTER TO MASTER_HOST='ip_from_master',
MASTER_USER='replica_user',
MASTER_PASSWORD='12345678',
MASTER_LOG_FILE='mysql-bin.000001',
MASTER_LOG_POS=154;