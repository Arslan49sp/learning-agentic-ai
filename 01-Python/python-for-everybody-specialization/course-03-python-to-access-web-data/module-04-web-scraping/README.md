# 🌐 Programs that Surf the Web (Web Scraping with Python)
## Module 04 – Using Python to Access Web Data
### Python for Everybody Specialization

This module focuses on building programs that can:

- access web pages
- download data from the internet
- understand character encoding
- convert strings ↔ bytes
- parse HTML
- extract useful information
- perform web scraping using BeautifulSoup

Now Python is not just reading local files —
👉 it can **crawl the internet and collect real-world data automatically**.

This is a core skill for:
- Web scraping
- Automation
- APIs
- Data engineering
- AI/Agentic systems

---

# 🎯 Module Objectives

After completing this module, I can:

✅ Understand ASCII and Unicode  
✅ Convert strings ↔ bytes  
✅ Use encode() and decode()  
✅ Fetch web pages using urllib  
✅ Handle URL errors  
✅ Parse HTML  
✅ Extract links and data  
✅ Use BeautifulSoup for scraping  

---

# 🧠 Character Encoding Basics

Before scraping the web, we must understand **text encoding**.

Computers store everything as:
👉 binary (0s and 1s)

So characters must be converted into numbers.

---

# 🔤 ASCII

ASCII = American Standard Code for Information Interchange

Uses:
```
7 bits → 128 characters
```

Includes:
- English letters
- numbers
- symbols

Examples:

| Character | ASCII Code |
|-----------|-------------|
| A | 65 |
| a | 97 |
| 0 | 48 |

Problem:
❌ Only English supported

---

# 🌍 Unicode

Unicode solves ASCII limitations.

Supports:
✅ All languages  
✅ Emojis  
✅ Special symbols  

Examples:
- Urdu
- Arabic
- Chinese
- Emojis 😊

Common encodings:
- UTF-8 (most popular)
- UTF-16

👉 Almost every website today uses UTF-8

---

# 🔄 Strings vs Bytes in Python

This is VERY IMPORTANT for networking & web data.

## String
Human-readable text

```python
text = "Hello"
```

Type:
```
str
```

---

## Bytes
Machine-readable binary

```python
b"Hello"
```

Type:
```
bytes
```

---

# 🔁 Encoding and Decoding

## Encode (string → bytes)

```python
text = "Hello"
data = text.encode()
```

---

## Decode (bytes → string)

```python
data = b"Hello"
text = data.decode()
```

---

# ⚠️ Rule to Remember

👉 Network → bytes  
👉 Python text → string  

So:

When sending → encode  
When receiving → decode  

---

# 🌐 urllib Module

Python provides `urllib` to fetch data from the web easily.

Import:

```python
import urllib.request
import urllib.parse
import urllib.error
```

---

# 📥 Fetch a Web Page

## Simple Example

```python
import urllib.request

fhand = urllib.request.urlopen("http://example.com")

for line in fhand:
    print(line.decode().strip())
```

---

## What happens internally?

1. Open URL
2. Send HTTP request
3. Receive bytes
4. Decode to text
5. Process content

---

# 📦 urllib Submodules

## urllib.request
Fetch URLs

Used for:
- opening web pages
- downloading files

---

## urllib.parse
Work with URLs

Used for:
- encoding parameters
- splitting URLs
- building query strings

Example:

```python
import urllib.parse

params = {"q": "python"}
query = urllib.parse.urlencode(params)
print(query)
```

Output:
```
q=python
```

---

## urllib.error
Handle errors

Used for:
- network failures
- invalid URLs
- HTTP errors

Example:

```python
try:
    urllib.request.urlopen("http://wrong-url.com")
except urllib.error.URLError:
    print("Failed to fetch")
```

---

# 🧠 What is HTML Parsing?

HTML pages contain:

- tags
- attributes
- nested elements

Example:

```html
<a href="google.com">Google</a>
```

We often want:
👉 only the link or text

Parsing helps extract specific parts.

---

# 🕷️ What is Web Scraping?

Web scraping =

👉 automatically extracting information from websites using code

Instead of:
❌ copy-paste manually

We:
✅ automate extraction

---

# 🧪 Basic Scraping Without BeautifulSoup

You could use:

```python
re.findall()
```

But:
❌ messy  
❌ unreliable  
❌ breaks easily  

Not recommended for HTML.

---

# 🌟 Why BeautifulSoup?

BeautifulSoup is made for:

✅ HTML parsing  
✅ Easy navigation  
✅ Cleaner code  
✅ Robust extraction  

Much better than regex for HTML.

---

# 📦 Installing BeautifulSoup

```bash
pip install beautifulsoup4
```

---

# 📥 Using BeautifulSoup

## Basic Example

```python
import urllib.request
from bs4 import BeautifulSoup

url = "http://example.com"
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

print(soup.title)
```

---

# 🔗 Extract All Links

```python
tags = soup("a")

for tag in tags:
    print(tag.get("href", None))
```

Output:
```
http://google.com
http://github.com
```

---

# 🔍 Common BeautifulSoup Methods

| Method | Purpose |
|-------------|------------|
| soup('a') | find all tags |
| find() | first match |
| find_all() | all matches |
| get() | get attribute |
| text | get inner text |

---

# 🧠 Typical Scraping Workflow

```
1. Fetch webpage (urllib)
2. Decode data
3. Parse HTML (BeautifulSoup)
4. Extract required data
5. Store/process results
```

---

# 🧪 Full Example Program

```python
import urllib.request
from bs4 import BeautifulSoup

url = "http://example.com"

html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

links = soup("a")

for link in links:
    print(link.get("href"))
```

---

# 🔥 Real World Use Cases

Web scraping is used for:

✅ Price comparison  
✅ Job listings  
✅ News aggregation  
✅ Data collection  
✅ Market research  
✅ SEO tools  
✅ AI training datasets  

---

# ⚠️ Best Practices

✅ Respect robots.txt  
✅ Don’t overload servers  
✅ Add delays between requests  
✅ Handle errors properly  
✅ Use BeautifulSoup instead of regex  
✅ Always decode bytes  

---

# 🚀 How This Module Helps My Journey

This module prepares me for:

- Web scraping
- API calls
- Automation bots
- Data pipelines
- AI agents that fetch live information
- Backend development

Now my Python programs can **surf the internet and collect real data automatically**.

This is a huge step toward:
👉 Agentic AI systems that gather information themselves

---

# 🧠 Quick Cheatsheet

```python
# encode / decode
text.encode()
data.decode()

# fetch url
urllib.request.urlopen(url)

# parse html
BeautifulSoup(html, "html.parser")

# get links
soup("a")
tag.get("href")
```

---

# ✨ Final Summary

In this module I learned:

✔ ASCII & Unicode  
✔ Strings vs Bytes  
✔ Encoding & decoding  
✔ urllib (request, parse, error)  
✔ HTML parsing  
✔ Web scraping  
✔ BeautifulSoup  

Now I can build programs that automatically download and extract data from the web.

This is a core foundation for:
👉 Scraping  
👉 APIs  
👉 Automation  
👉 Agentic AI  

---

## 👨‍💻 Author

Arslan  
Learning Python → Web → AI → Agentic Systems 🚀
