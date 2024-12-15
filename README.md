# <p font-size="2rem" align='center'>Student Management System CLI</p>

## Overview

The Student Management System CLI is a Python-based Command-Line Interface (CLI) application that facilitates the management of student and teacher records in a MySQL database. It allows users to perform CRUD (Create, Read, Update, Delete) operations on records, categorized by user roles such as Admin, Teacher, and Student, with varying access permissions. Operations performed are logged into a database table for tracking purposes.

## Features

### _User Role-Based Authentication:_

- Admin: Full access to both students and teachers tables.
- Teacher: Access to perform CRUD operations on the students table.
- Student: Read-only access to the students table.
- CRUD Operations:
  - Create: Add new records to the database.
  - Read: View existing records.
  - Update: Modify existing records.
  - Delete: Remove records from the database.

### _Operation Logging:_

All operations are logged into the operation_logs table with details such as operation type, table name, user role, and timestamp.

## Prerequisites

### _Software Requirements:_

- Python 3.8 or later
- MySQL Server
- Python Libraries
  - mysql-connector-python
  - Install the required library using: <code> pip install mysql-connector-python</code>

## Flow of Execution

### _Database Setup:_

- Create the Database and Tables.
- Insert the data into the tables.
- Refer to the **database_setup.sql** file for the commands.
- Ensure that the database credentials in the code (host, user, password, and database) match your MySQL setup.
- Execute the Python script: <code>python student_management_system.py</code>
