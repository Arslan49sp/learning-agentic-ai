# 🌍 JSON and the REST Architecture
## Module 06 – Using Python to Access Web Data
### Python for Everybody Specialization

This module focuses on how **modern applications communicate over the internet** using:

- JSON
- APIs
- REST architecture
- Service-oriented systems

Instead of scraping web pages or parsing XML, we now interact with:

👉 clean, structured, machine-to-machine data services

This is how almost all modern software works:
- mobile apps
- web apps
- cloud services
- AI systems
- payment gateways
- social media platforms

Everything runs on:
👉 APIs + JSON

---

# 🎯 Module Objectives

After completing this module, I can:

✅ Understand JSON format  
✅ Convert JSON ↔ Python objects  
✅ Use json.loads() and json.dumps()  
✅ Understand Service-Oriented Architecture (SOA)  
✅ Understand APIs  
✅ Work with REST services  
✅ Fetch data from web APIs using Python  

---

# 🧠 Big Picture: Evolution of Web Data

## Step 1
HTML → for humans (messy for programs)

## Step 2
XML → structured but heavy

## Step 3 (Modern)
JSON → lightweight, fast, easy

👉 Today almost all APIs use JSON

---

# 📦 What is JSON?

JSON = JavaScript Object Notation

Used for:
👉 storing and transferring structured data

It looks like Python dictionaries.

---

# 🔤 JSON Example

```json
{
    "name": "Arslan",
    "age": 25,
    "is_student": true,
    "skills": ["Python", "Web", "AI"]
}
```

---

# 🧩 JSON Data Types

| JSON Type | Python Equivalent |
|------------|------------------|
| object | dict |
| array | list |
| string | str |
| number | int/float |
| true/false | True/False |
| null | None |

---

# 🔁 JSON ↔ Python Conversion

Python provides:

```python
import json
```

---

# 📥 json.loads() (Decode JSON → Python)

Loads JSON string into Python object

```python
import json

data = '{"name": "Arslan", "age": 25}'

info = json.loads(data)

print(info["name"])
print(info["age"])
```

Output:
```
Arslan
25
```

---

# 📤 json.dumps() (Encode Python → JSON)

Converts Python object into JSON string

```python
import json

person = {
    "name": "Arslan",
    "age": 25
}

data = json.dumps(person)

print(data)
```

---

# 🧠 Rule to Remember

👉 Receiving data → loads()  
👉 Sending data → dumps()  

---

# 📂 Nested JSON Example

```json
{
  "users": [
    {"name": "Ali", "age": 20},
    {"name": "Sara", "age": 22}
  ]
}
```

---

## Python Access

```python
info = json.loads(data)

for user in info["users"]:
    print(user["name"])
```

---

# 🌐 What is an API?

API = Application Programming Interface

It allows:
👉 programs to talk to other programs

Instead of:
❌ scraping websites

We:
✅ request data directly from servers

---

# 📌 Examples of APIs

- Weather API
- Google Maps API
- GitHub API
- Stripe API
- Twitter API
- OpenAI API

Almost all return:
👉 JSON

---

# 🔁 How API Communication Works

```
Client → HTTP Request → Server
Client ← JSON Response ← Server
```

---

# 🧪 Calling an API in Python

## Example

```python
import urllib.request
import json

url = "https://api.github.com"

response = urllib.request.urlopen(url).read()

data = json.loads(response.decode())

print(data)
```

---

# 🌍 Service-Oriented Architecture (SOA)

SOA means:

👉 system built using independent services

Each service:
- does one job
- communicates via network
- returns data

---

## Example

Instead of one big app:

```
User Service
Payment Service
Auth Service
Weather Service
```

Each service has its own API.

---

# 🧠 Why SOA?

Benefits:

✅ modular  
✅ scalable  
✅ reusable  
✅ easier maintenance  
✅ independent deployment  

Used by:
- Google
- Amazon
- Netflix
- Uber
- almost every big tech company

---

# 🌐 What is REST?

REST = Representational State Transfer

It is a design style for APIs.

Most modern APIs are:
👉 RESTful APIs

---

# 🔑 REST Principles

## 1. Use HTTP methods

| Method | Action |
|-----------|-------------|
| GET | retrieve data |
| POST | create data |
| PUT | update data |
| DELETE | remove data |

---

## 2. Resources via URLs

Example:

```
/users
/users/1
/products
/orders/10
```

---

## 3. Stateless

Each request:
- independent
- contains all info needed

Server does not remember previous requests.

---

## 4. JSON responses

Most REST APIs return:
👉 JSON

---

# 🧪 REST API Example

## Request

```
GET /users/1
```

## Response

```json
{
    "id": 1,
    "name": "Arslan"
}
```

---

# 🛠️ Typical API Workflow

```
1. Send HTTP request
2. Receive JSON response
3. Decode using json.loads()
4. Extract needed data
5. Use in program
```

---

# 🔥 Real World Use Cases

JSON + REST are used in:

✅ Mobile apps  
✅ Web apps  
✅ Cloud services  
✅ Payment systems  
✅ AI agents  
✅ Chatbots  
✅ SaaS platforms  
✅ Data pipelines  

Almost everything today uses APIs.

---

# 🆚 JSON vs XML

| Feature | JSON | XML |
|------------|------------|------------|
| Size | small | large |
| Speed | fast | slower |
| Readability | easy | complex |
| Popularity | very high | medium |
| Modern APIs | yes | rare |

👉 JSON is preferred today

---

# ⚠️ Best Practices

✅ Always decode bytes → string  
✅ Handle API errors  
✅ Check status codes  
✅ Use try/except  
✅ Respect rate limits  
✅ Avoid scraping when API exists  
✅ Use JSON for modern apps  

---

# 🚀 How This Module Helps My Journey

This module prepares me for:

- Working with real APIs
- Backend development
- Cloud services
- Automation
- AI integrations
- Agentic systems that fetch live data

Now I can:

👉 talk directly to services  
👉 request structured data  
👉 build intelligent programs  

This is exactly how:
- ChatGPT
- Stripe
- GitHub
- Weather apps
work internally.

---

# 🧠 Quick Cheatsheet

```python
import json
import urllib.request

data = urllib.request.urlopen(url).read()

info = json.loads(data.decode())

json.dumps(python_object)
```

---

# ✨ Final Summary

In this module I learned:

✔ JSON format  
✔ loads() and dumps()  
✔ APIs  
✔ Service-oriented architecture  
✔ REST principles  
✔ Fetching API data  

Now I can build programs that communicate directly with web services using structured data.

This is the foundation of:
👉 Modern web development  
👉 Cloud apps  
👉 Automation  
👉 Agentic AI systems  

---

# 🎉 Course Completion

With this module, I have completed:

✅ Networking & sockets  
✅ Web scraping  
✅ XML  
✅ JSON  
✅ APIs  
✅ REST  

Now my Python skills are ready for:
👉 real-world backend + AI agent development

---

## 👨‍💻 Author

Arslan Majeed 
Learning Python → Web → AI → Agentic Systems 🚀
