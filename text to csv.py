import pandas as pd
from io import StringIO

# CSV text data
csv_text = """
Question,Choice A,Choice B,Choice C,Choice D,Correct Answer,Reason,Marks
"What is the most commonly used open-source relational database management system (RDBMS)?",MySQL,PostgreSQL,SQLite,Oracle,A,"MySQL is an open-source relational database management system (RDBMS) commonly used in web development.",1
"What uniquely identifies each record in a database table?",Primary Key,Foreign Key,Super Key,Composite Key,A,"Primary key uniquely identifies each record in a database table.",1
"Which SQL command is used to retrieve data from a database?",SELECT,FROM,WHERE,JOIN,A,"SELECT is used to retrieve data from a database.",1
"Which process involves adding redundant data to a normalized database to improve read performance?",Denormalization,Normalization,Optimization,Indexing,A,"Denormalization involves adding redundant data to a normalized database to improve read performance.",1
"What does ACID stand for in the context of database transactions?",ACID,BCNF,CRUD,OLAP,A,"ACID stands for Atomicity, Consistency, Isolation, and Durability, which are the four key properties of a transaction in a database.",1
"Which type of database is designed to store and retrieve data that doesn't require a fixed schema like relational databases?",NoSQL,SQL,XML,JSON,A,"NoSQL databases are designed to store and retrieve data that doesn't require a fixed schema like relational databases.",1
"What is the software suite designed to manage databases called?",Database Management System (DBMS),Structured Query Language (SQL),Entity-Relationship Diagram (ERD),Data Definition Language (DDL),A,"DBMS is a software suite designed to manage databases.",1
"Which SQL command is used to modify existing records in a database table?",UPDATE,INSERT,ALTER,CREATE,A,"UPDATE is used to modify existing records in a database table.",1
"What organizes data into tables consisting of rows and columns?",Relational Model,Network Model,Document Model,Object-Oriented Model,A,"The relational model organizes data into tables consisting of rows and columns.",1
"Which is used to manage simultaneous access to a database by multiple users or transactions?",Concurrency Control,Data Mining,Data Warehousing,Data Encryption,A,"Concurrency control is used to manage simultaneous access to a database by multiple users or transactions.",1
"Which are data structures used to improve the speed of data retrieval operations on a database table?",Indexes,Views,Stored Procedures,Triggers,A,"Indexes are data structures used to improve the speed of data retrieval operations on a database table.",1
"Which involves making copies of data to protect against data loss due to hardware failures, human errors, or disasters?",Backup,Normalization,Transaction,Locking,A,"Backup involves making copies of data to protect against data loss due to hardware failures, human errors, or disasters.",1
"What represents a single data item in a database table?",Row,Table,Column,Database,A,"A row, also known as a record, represents a single data item in a database table.",1
"Which refers to a field in a database table that refers to the primary key of another table?",Foreign Key,Primary Key,Unique Key,Composite Key,A,"A foreign key is a field in a database table that refers to the primary key of another table.",1
"What is the process of organizing data in a database to minimize redundancy and dependency?",Normalization,Denormalization,Optimization,Indexing,A,"Normalization is the process of organizing data in a database to minimize redundancy and dependency.",1
"Which SQL command is used to define and create database objects such as tables, indexes, views, and stored procedures?",CREATE,UPDATE,DELETE,INSERT,A,"CREATE is used to define and create database objects such as tables, indexes, views, and stored procedures.",1
"Which theoretical framework is used for reasoning about the properties of relational database operations?",Relational Algebra,Data Manipulation Language (DML),Structured Query Language (SQL),Data Definition Language (DDL),A,"Relational algebra is a theoretical framework used for reasoning about the properties of relational database operations.",1
"What is a domain-specific language used in programming and designed for managing and querying relational databases?",Structured Query Language (SQL),Database Management System (DBMS),Entity-Relationship Diagram (ERD),Data Definition Language (DDL),A,"SQL is a domain-specific language used in programming and designed for managing and querying relational databases.",1
"What is a special type of stored procedure that automatically executes in response to certain events or actions on a database table?",Trigger,Stored Procedure,View,Index,A,"A trigger is a special type of stored procedure that automatically executes in response to certain events or actions on a database table.",1
"What defines the structure of a database, including tables, columns, relationships, indexes, and constraints?",Database Schema,Data Warehouse,Data Model,Data Dictionary,A,"A database schema is a blueprint that defines the structure of a database, including tables, columns, relationships, indexes, and constraints.",1
"""

# Convert CSV text to DataFrame
df = pd.read_csv(StringIO(csv_text))

# Write DataFrame to Excel file
excel_filename = "database_quiz.xlsx"
df.to_excel(excel_filename, index=False)

print("Excel file created successfully:", excel_filename)
