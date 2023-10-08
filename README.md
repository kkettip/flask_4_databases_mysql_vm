# flask_4_databases_mysql_vm

####**.env file includes the following:**

DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

#### **MySQL Setup on Azure VM**
**Steps:**
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
Select Action: Allow
20. Name port or use default name
21. Select  Add
