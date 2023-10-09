# flask_4_databases_mysql_vm

**.env file includes the following:**

`DB_HOST=your_host`

`DB_DATABASE=your_database_name`

`DB_USERNAME=your_username`

`DB_PASSWORD=your_password`

`DB_PORT=3306`

`DB_CHARSET=utf8mb4`



#### **MySQL Setup on Azure VM**

**Create Azure Virtual Machine (VM)**

Steps:
1. Login into Azure
2. Select: Virtual Machines 
3. Select: Create 
4. Select: Azure virtual machine
5. Select: Resource Group or create a new Resource Group
6. Name virtual machine
7. Select: Region: (US) East US
8. Select: Availability options, Availability zone, Security type, image, VM architecture and Run with Azure Spot Discount or leave at default settings
9. Select: Size
10. Select: Authentication type: Password 
11. Setup Username and Password for VM
12. Select Public inbound sports: Allow selected ports 
13. Select inbound ports: SSH(22), HTTP(80) and HTTPS(443) 
14. Select: Review + create 
15. Select: Create
16. Once the VM is created, go to Networking. 
17. Select: Add inbound port rule 
18. Select: Service: MySQL port 3306 is automatically populated
19. Select:Source, source port ranges, destination, protocol, priority or leave at default settings
20. Select Action: Allow
21. Name port or use default name
22. Select  Add

**Connect Cloud Shell environment to VM** 

In Cloud Shell
1. Input VM information: `ssh <username>@<public-ip-address>` 
2. Input VM password 
3. Input `sudo apt-get update to update` the UBUNTU (OS) SERVER 
4. Input `sudo apt-get install mysql-server mysql-client` to install MySQL server and client 
5. Input Y 
6. Input `sudo mysql` to log into MySQL
7. To create a new user and grant privileges to the user: Input `CREATE USER ‘user'@'%' IDENTIFIED BY ‘password’;` and `GRANT ALL PRIVILEGES ON *.* TO ‘user'@'%’ WITH GRANT OPTION;`
8. Exit MySQL.
9. To edit the MySQL configuration file and change the bind-address to 0.0.0.0. 
10. Input: `sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf` and change the bind-address to 0.0.0.0.
11. Save the file and exit.
12. To restart: Input: `sudo service mysql restart`

**Connect MySQL Workbench to VM**

In MySQL Workbench 
1. Select: `+` at home screen to create a new MySQL connection 
2. Setup Connection name
3. Input:  VM's Hostname: public IP address, username and password
4. Select: Test Connection
5. Select: OK

**Database Schema**

Database name: all_patients

Tables: patients, conditions and patient_conditions

The relationship type is many to many because one patient can be associated with many types of conditions. The junction table is the conditions table. The junction table has a one to many relationship with the patient_conditions table. The patients and conditions table has a one to many relationship with patient_conditions table. The junction table allows one to manage the relationships between the patients and conditions table.

**Steps and challenges**

To connect with Flask 

1. Import the following libaries: 

`from flask import Flask, render_template`

`from pandas import read_sql`

`import pandas as pd`

`import os`

`from dotenv import load_dotenv`

`from sqlalchemy import create_engine, inspect`

`import sqlalchemy`

2. Connect to mysql database with `conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}")`

3. Create database engine with `db_engine = create_engine(conn_string, echo=False)`

Errors

1. Error enountered prevented insertion of fake data into table with the error message: ObjectNotExecutableError: Not an executable object: "INSERT INTO patients (first_name, last_name, date_of_birth) VALUES ('Susan', 'Romero', '1934-06-16')" 

Error was resolved with the solution found from stack overflow to downgrade sqlalchemy by `pip install sqlalchemy==1.4.46`

2. Typo in port number prevented connection with Flask. Inputting correct port number resolved the issue.



