# 📘 Module 03 — Data Models and Relational SQL

This module focuses on how to design structured databases and work with relational data using SQL.

It covers:
- Database design
- Data modeling
- Keys (Primary, Foreign, Logical)
- Inserting relational data
- Reconstructing data using JSON
- JOIN operations

---

# 1️⃣ Database Design

## 🔹 What is Database Design?

Database design is the process of organizing data into tables in a way that:

- Minimizes redundancy
- Maintains consistency
- Improves performance
- Supports scalability

A good database design ensures:

- Efficient data storage
- Easy data retrieval
- Logical relationships between data

---

## 🔹 Goals of Database Design

- Avoid duplicate data
- Maintain data integrity
- Improve query performance
- Make system scalable

---

# 2️⃣ Data Modeling

## 🔹 What is a Data Model?

A data model represents how data is structured and related.

It defines:

- Entities (tables)
- Attributes (columns)
- Relationships (links between tables)

---

## 🔹 Example: Track Management Data Model

Suppose we are building a music system.

We may have:

- Artist
- Album
- Track

---

### 🔹 Logical Representation

- One Artist → Many Albums  
- One Album → Many Tracks  

---

# 3️⃣ Representing Data Models in Tables

We convert the data model into relational tables.

---

## 🔹 Example Tables

### Artist Table

| id | name |
|----|------|

---

### Album Table

| id | title | artist_id |
|----|--------|-----------|

---

### Track Table

| id | title | album_id |
|----|--------|-----------|

---

## 🔹 Relationships

- Artist → Album (1-to-Many)
- Album → Track (1-to-Many)

---

# 4️⃣ Keys in Relational Databases

## 🔹 Primary Key

- Uniquely identifies each row
- Cannot be NULL
- Must be unique

Example:
```sql
id INTEGER PRIMARY KEY
```

---

## 🔹 Foreign Key

- Links one table to another
- References a primary key in another table

Example:
```sql
artist_id REFERENCES Artist(id)
```

---

## 🔹 Logical Key

- A field that uniquely identifies data logically
- Not necessarily used as primary key

Example:
- Email
- Username

---

# 5️⃣ Creating Tables with Relationships

```sql
CREATE TABLE Artist (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE Album (
    id INTEGER PRIMARY KEY,
    title TEXT,
    artist_id INTEGER
);

CREATE TABLE Track (
    id INTEGER PRIMARY KEY,
    title TEXT,
    album_id INTEGER
);
```

---

# 6️⃣ Inserting Relational Data

Data must be inserted in order based on relationships.

---

## 🔹 Step 1: Insert Parent Table

```sql
INSERT INTO Artist (name) VALUES ('Arijit Singh');
```

---

## 🔹 Step 2: Insert Child Table

```sql
INSERT INTO Album (title, artist_id)
VALUES ('Album 1', 1);
```

---

## 🔹 Step 3: Insert Related Data

```sql
INSERT INTO Track (title, album_id)
VALUES ('Song 1', 1);
```

---

## 🔹 Important Rule

👉 Always insert data in parent tables first, then child tables.

---

# 7️⃣ Reconstructing Data with JSON

Relational data is stored in multiple tables.

Sometimes we need to reconstruct it into a structured format like JSON.

---

## 🔹 Example Goal

Convert relational data into:

```json
{
  "artist": "Arijit Singh",
  "albums": [
    {
      "title": "Album 1",
      "tracks": ["Song 1", "Song 2"]
    }
  ]
}
```

---

## 🔹 Why Reconstruct?

- APIs return JSON
- Easier for frontend
- Structured representation of relationships

---

# 8️⃣ JOIN Operations

JOIN is used to combine data from multiple tables.

---

## 🔹 Why JOIN?

Because relational data is stored separately.

JOIN allows us to:

- Combine tables
- Retrieve meaningful data
- Rebuild relationships

---

# 9️⃣ Types of JOIN (Basic Focus)

## 🔹 JOIN with ON Clause

Used to define relationship explicitly.

```sql
SELECT Track.title, Album.title
FROM Track
JOIN Album ON Track.album_id = Album.id;
```

---

## 🔹 JOIN Multiple Tables

```sql
SELECT Track.title, Artist.name
FROM Track
JOIN Album ON Track.album_id = Album.id
JOIN Artist ON Album.artist_id = Artist.id;
```

---

## 🔹 JOIN without ON Clause

Uses WHERE condition.

```sql
SELECT Track.title, Album.title
FROM Track, Album
WHERE Track.album_id = Album.id;
```

---

## 🔹 Difference

| Method | Description |
|--------|------------|
| JOIN ... ON | Modern, cleaner |
| WHERE | Older style |

👉 Prefer `JOIN ... ON`

---

# 🔟 Data Flow in Relational Systems

```
Tables → Relationships → JOIN → Result → JSON/API
```

---

# 📌 Module Summary

In this module, you learned:

- Database design principles
- Data modeling
- Converting models into tables
- Primary key, foreign key, logical key
- Inserting relational data
- Reconstructing data using JSON
- JOIN operations (with and without ON)

This is the core of:

- Backend development
- API design
- Data engineering
- Scalable systems

---

# 🎯 Interview Questions & Answers

## ❓ What is a relational database?

A relational database stores data in tables and establishes relationships between them using keys.

---

## ❓ What is a primary key?

A primary key uniquely identifies each row in a table and cannot be NULL.

---

## ❓ What is a foreign key?

A foreign key is a field in one table that refers to the primary key of another table.

---

## ❓ What is a data model?

A data model defines how data is structured, stored, and related in a database.

---

## ❓ What is normalization?

Normalization is the process of organizing data to reduce redundancy and improve consistency.

---

## ❓ Why do we use JOIN?

JOIN is used to combine data from multiple tables based on relationships.

---

## ❓ Difference between JOIN and WHERE?

- JOIN uses ON clause (modern)
- WHERE uses condition-based matching (older)

---

## ❓ What is the difference between logical key and primary key?

- Logical key: meaningful unique field (e.g., email)
- Primary key: technical unique identifier

---

## ❓ Why insert parent table data first?

Because child tables depend on foreign keys referencing parent tables.

---

## ❓ What is reconstructing data?

It means combining relational data from multiple tables into structured formats like JSON.

---

## ❓ Why is database design important?

Because it ensures:

- Efficient storage
- Data consistency
- Scalability
- Better performance

---

# 🚀 Final Takeaway

This module is one of the most important parts of backend development.

Now you understand:

- How real-world data is modeled
- How tables are connected
- How to retrieve meaningful data
- How to transform relational data into structured formats

This is the foundation for:

- APIs
- Backend systems
- Data-driven applications
- AI systems with structured data

---

## 👨‍💻 Author

Arslan  
Learning Python → Web → Databases → AI → Agentic Systems 🚀
