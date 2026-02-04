# 🌐 Network and Sockets in Python
## Module 03 – Using Python to Access Web Data
### Python for Everybody Specialization

This module explains **how computers communicate over the internet**.

Before using high-level tools like `requests` or APIs, we first understand:

- how data travels
- how connections are created
- what ports are
- how TCP works
- how sockets work internally
- how HTTP sends web pages

This knowledge builds the **foundation of web scraping, backend development, APIs, and Agentic AI systems**.

---

# 🎯 Module Objectives

After completing this module, I can:

✅ Understand TCP/IP basics  
✅ Understand ports and their purpose  
✅ Identify common TCP ports  
✅ Create sockets in Python  
✅ Connect to remote servers manually  
✅ Send HTTP requests using sockets  
✅ Understand how browsers fetch web pages  

---

# 🧠 Big Picture: How the Internet Works

When you open a website:

```
Browser → Internet → Server → Response → Browser
```

Behind the scenes:

1. Client sends request
2. Server listens on a port
3. TCP connection established
4. Data is transferred
5. Connection closed

---

# 🌍 What is a Network?

A network is a group of devices connected to share data.

Examples:
- Internet
- LAN
- WiFi network

Each device has:
- IP address → identifies machine
- Port → identifies application

---

# 📌 IP Address

An IP address uniquely identifies a device.

Example:
```
142.250.183.14
```

Like a **home address for computers**.

---

# 🚪 What is a Port?

A port identifies a **specific service/application** running on a device.

Think of it like:

```
IP = Building address
Port = Apartment number
```

Without ports → server wouldn't know which app should receive data.

---

# 🔢 Common TCP Ports (Very Important)

| Port | Service |
|--------|-----------|
| 20/21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP (Email) |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 3306 | MySQL |

---

# 🔗 TCP Protocol

## What is TCP?

TCP = Transmission Control Protocol

It ensures:

✅ Reliable  
✅ Ordered  
✅ Error-checked  
✅ Complete delivery  

---

## TCP Features

- Connection-oriented
- Data arrives in order
- Retransmits lost packets
- Reliable communication

---

## TCP 3-Way Handshake

Connection setup:

```
Client → SYN
Server → SYN-ACK
Client → ACK
```

After this → connection established

---

# 🧦 What is a Socket?

A socket is an **endpoint of communication** between two machines.

It allows:
- sending data
- receiving data

Socket = doorway between client and server

---

# 📦 Python socket Module

Python provides:

```python
import socket
```

Used for low-level network communication.

---

# 🛠️ Creating a Socket in Python

## Basic Steps

1. Create socket
2. Connect to server
3. Send request
4. Receive response
5. Close connection

---

## Example: Simple Connection

```python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect(("example.com", 80))

mysock.close()
```

---

## Socket Types

### AF_INET
IPv4 addressing

### SOCK_STREAM
TCP protocol

Common combo:
```python
socket.AF_INET, socket.SOCK_STREAM
```

---

# 🌐 HTTP Protocol

HTTP = HyperText Transfer Protocol

Used for:
- websites
- APIs
- web communication

It works on:
```
Port 80 (HTTP)
Port 443 (HTTPS)
```

---

# 📤 HTTP Request Structure

Example request:

```
GET / HTTP/1.1
Host: example.com
```

---

# 📥 HTTP Response Structure

Example:

```
HTTP/1.1 200 OK
Content-Type: text/html

<html>...</html>
```

---

## Common HTTP Methods

| Method | Purpose |
|-----------|-------------|
| GET | retrieve data |
| POST | send data |
| PUT | update |
| DELETE | remove |

---

# 🧪 Manual HTTP Request using Socket ⭐

This shows how browsers actually work internally.

```python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))

cmd = "GET /romeo.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

mysock.close()
```

---

## What happens here?

Step-by-step:

1. Create socket
2. Connect to server
3. Send HTTP GET request
4. Receive chunks of data
5. Print response
6. Close socket

---

# 🔁 recv() Explanation

```python
mysock.recv(512)
```

Means:
👉 receive 512 bytes at a time

Because data is sent in chunks.

---

# 📊 Flow of Data

```
Client (Python script)
        ↓
Socket connection
        ↓
HTTP request
        ↓
Server response
        ↓
HTML/Text data
```

---

# 🔥 Real World Usage

Sockets are used for:

✅ Web browsers  
✅ Chat apps  
✅ Multiplayer games  
✅ APIs  
✅ Email systems  
✅ Streaming  
✅ IoT devices  

---

# 🆚 Sockets vs High-Level Libraries

## Using sockets (low level)

```python
socket
```

Pros:
- full control
- understand internals

Cons:
- more code

---

## Using requests (high level)

```python
import requests
```

Pros:
- easy
- fast
- clean

Cons:
- hides internals

---

👉 In real projects → use `requests`  
👉 For learning → sockets are gold

---

# ⚠️ Best Practices

✅ Always close socket  
✅ Use HTTPS when possible  
✅ Handle errors  
✅ Use libraries for production  
✅ Understand low-level first (like now)

---

# 🚀 How This Module Helps My Journey

This module prepares me for:

- Web scraping
- API calls
- Backend development
- Network debugging
- Building AI agents that fetch live data
- Understanding how the web really works

Without this knowledge, high-level tools feel like magic.  
Now I know what’s happening underneath.

---

# 🧠 Quick Cheatsheet

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("example.com", 80))
s.send(b"GET / HTTP/1.0\r\n\r\n")
data = s.recv(512)
s.close()
```

---

# ✨ Final Summary

In this module I learned:

✔ TCP basics  
✔ Ports  
✔ Common services  
✔ Sockets  
✔ HTTP  
✔ Manual web requests  

Now I understand how data travels from my Python script to a server and back.

This is the foundation of:
👉 Web scraping  
👉 APIs  
👉 Automation  
👉 Agentic AI systems  

---

## 👨‍💻 Author

Arslan  
Learning Python → Web → AI → Agentic Systems 🚀
