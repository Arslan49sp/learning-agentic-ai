# 📘 Module 02 — Basic Structured Query Language (SQL)

This module covers the foundational concepts of relational databases and Structured Query Language (SQL).

---

# 1️⃣ Databases

## 🔹 What is a Database?

A database is an organized collection of data that can be:

- Stored
- Managed
- Retrieved
- Updated

Databases are used in:

- Web applications
- Mobile apps
- Banking systems
- E-commerce platforms
- Enterprise systems

---

# 2️⃣ Relational Databases

## 🔹 What is a Relational Database?

A relational database stores data in the form of tables.

Each table:
- Has rows and columns
- Stores structured data
- Maintains relationships with other tables

Data is organized in relations (tables), which is why it is called a relational database.

---

## 🔹 Table Structure

A table consists of:

- Rows → Records
- Columns → Fields
- First row → Schema (Structure of table)

---

## 🔹 Schema

Schema defines:

- Table name
- Column names
- Data types
- Constraints

Example:

| id | name | age |
|----|------|-----|

Here, `id`, `name`, and `age` form the schema.

Schema defines how data is structured.

---

# 3️⃣ SQL (Structured Query Language)

## 🔹 What is SQL?

SQL (Structured Query Language) is used to:

- Create databases
- Create tables
- Insert data
- Retrieve data
- Update data
- Delete data

It is the standard language for relational databases.

---

## 🔹 Why SQL is Important

SQL allows:

- Communication between application and database
- Data manipulation
- Data querying
- Managing large datasets efficiently

---

# 4️⃣ CRUD Operations

CRUD stands for:

- C → Create
- R → Read
- U → Update
- D → Delete

These are the four basic database operations.

---

## 🔹 CREATE

Insert new data.

```sql
INSERT INTO students (name, age)
VALUES ('Ali', 22);
```

---

## 🔹 READ

Retrieve data.

```sql
SELECT * FROM students;
```

---

## 🔹 UPDATE

Modify existing data.

```sql
UPDATE students
SET age = 23
WHERE name = 'Ali';
```

---

## 🔹 DELETE

Remove data.

```sql
DELETE FROM students
WHERE name = 'Ali';
```

---

# 5️⃣ Roles in Database Systems

## 🔹 Application Developer

Responsible for:

- Writing application code
- Connecting application to database
- Performing CRUD operations
- Managing queries inside applications

Example:
- Backend developer using Python + MySQL

---

## 🔹 Database Administrator (DBA)

Responsible for:

- Database installation
- Security management
- Backup and recovery
- Performance tuning
- User access control

DBA ensures database reliability and availability.

---

# 6️⃣ Large Project Structure

In large systems:

- Application layer handles business logic
- Database layer stores and manages data
- Communication happens via SQL queries

Typical flow:

User → Application → Database → Application → User

Large projects may use:

- Multiple tables
- Relationships between tables
- Indexes for performance
- Separate environments (Dev, Test, Production)

---

# 7️⃣ Database Model / Schema

Database model defines:

- Table structures
- Relationships
- Primary keys
- Foreign keys

Schema acts as a blueprint for database design.

Good schema design ensures:

- Data consistency
- Reduced redundancy
- Better performance

---

# 8️⃣ Common Database Systems

## 🔹 Oracle
- Enterprise-level database
- Highly scalable
- Used in banking and large corporations

---

## 🔹 MySQL
- Open-source
- Widely used in web development
- Popular with PHP and Python

---

## 🔹 MariaDB
- Fork of MySQL
- Open-source
- High performance

---

## 🔹 Microsoft SQL Server
- Developed by Microsoft
- Common in enterprise Windows environments

---

## 🔹 SQLite
- Lightweight
- File-based
- Used in mobile apps and small applications

---

## 🔹 PostgreSQL
- Advanced open-source database
- Strong support for complex queries
- Highly reliable and scalable

---

# 9️⃣ Single Table CRUD

Basic operations performed on a single table:

Example Table: `students`

---

## 🔹 Create Table

```sql
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT
);
```

---

## 🔹 Insert Data

```sql
INSERT INTO students (name, age)
VALUES ('Ahmed', 21);
```

---

## 🔹 Select Data

```sql
SELECT * FROM students;
```

---

## 🔹 Update Data

```sql
UPDATE students
SET age = 22
WHERE id = 1;
```

---

## 🔹 Delete Data

```sql
DELETE FROM students
WHERE id = 1;
```

---

# 🔟 Sorting with ORDER BY

Used to sort query results.

---

## 🔹 Ascending Order (Default)

```sql
SELECT * FROM students
ORDER BY age ASC;
```

---

## 🔹 Descending Order

```sql
SELECT * FROM students
ORDER BY age DESC;
```

---

# 1️⃣1️⃣ Using MySQL Database in Python

Python can connect to MySQL using libraries such as:

- mysql-connector-python
- PyMySQL

---

## 🔹 Basic Connection Example

```python
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="school"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

connection.close()
```

---

## 🔹 Steps to Use MySQL in Python

1. Install connector library
2. Establish connection
3. Create cursor
4. Execute SQL query
5. Fetch results
6. Close connection

---

# 📌 Module Summary

In this module, you learned:

- What databases are
- Relational database structure
- Schema and table design
- SQL and its usage
- CRUD operations
- Roles: Application Developer & DBA
- Large project structure
- Common database systems
- Single table CRUD operations
- Sorting using ORDER BY
- Connecting MySQL with Python

This module builds the foundation for:

- Backend development
- API development
- Full-stack systems
- Data-driven applications

---

## 👨‍💻 Author

Arslan  
Learning Python → Web → Databases → AI → Agentic Systems 🚀