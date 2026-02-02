# 🔍 Regular Expressions (Regex) in Python
## Module 02 – Using Python to Access Web Data
### Python for Everybody Specialization

Regular Expressions (Regex) are powerful tools used to **search, match, extract, and clean text data** using patterns.

When working with:
- web pages
- scraped HTML
- logs
- APIs
- emails
- messy text files

Regex becomes extremely useful for **finding specific information inside large data**.

This module builds the foundation for **web scraping, automation, and AI data pipelines**.

---

# 🎯 Module Objectives

After completing this module, I can:

✅ Search inside large text  
✅ Extract specific patterns (numbers, emails, links, etc.)  
✅ Use Python `re` module  
✅ Use `search()`, `findall()`, `match()`  
✅ Apply regex symbols and pattern rules  
✅ Understand greedy vs non-greedy matching  
✅ Clean messy web data efficiently  

---

# 📦 Python Regex Module

Python provides built-in support using:

```python
import re
```

All regex operations are done through this module.

---

# 🧠 Why Regex?

Without regex:
👉 manual loops, conditions, string splitting (slow & messy)

With regex:
👉 1 line solution

Example:

```python
re.findall(r"\d+", text)
```

Extracts all numbers instantly.

---

# 🔎 Core Functions

## 1️⃣ re.search()

Finds the **first match only**

```python
re.search(pattern, text)
```

Example:

```python
import re

text = "My number is 12345"

match = re.search(r"\d+", text)

if match:
    print(match.group())
```

---

## 2️⃣ re.findall() ⭐ (MOST IMPORTANT)

Returns **all matches as a list**

```python
re.findall(pattern, text)
```

Example:

```python
text = "Marks: 78, 90, 85"

numbers = re.findall(r"\d+", text)
print(numbers)
```

Output:
```
['78', '90', '85']
```

👉 Most useful function for data extraction & scraping

---

## 3️⃣ re.match()

Matches only at the **start of string**

```python
re.match(pattern, text)
```

Example:

```python
re.match("Hello", "Hello world")  ✅
re.match("world", "Hello world")  ❌
```

---

# 🔤 Basic Pattern Rules

## Literal Match

```python
re.findall("cat", text)
```

Matches exact word "cat"

---

# 🔡 Character Classes

## Square Brackets []

Match any one character inside brackets.

| Pattern | Meaning |
|---------|----------|
| [0-9] | digits |
| [a-z] | lowercase letters |
| [A-Z] | uppercase letters |
| [A-Za-z] | all letters |
| [^0-9] | NOT digits |

Example:

```python
re.findall(r"[A-Za-z]+", text)
```

---

# ⚡ Shortcuts (Very Common)

| Symbol | Meaning |
|----------|------------|
| \d | digit (0-9) |
| \D | not digit |
| \w | word character |
| \W | not word |
| \s | whitespace |
| \S | not whitespace |
| . | any character |

Example:

```python
re.findall(r"\d+", text)
```

---

# 🔁 Repetition Symbols

Used to control quantity.

| Symbol | Meaning |
|-----------|--------------|
| + | one or more |
| * | zero or more |
| ? | optional |
| {n} | exactly n times |
| {n,m} | between n and m |

Examples:

```python
\d+      # one or more digits
\d*      # zero or more digits
\d{3}    # exactly 3 digits
```

---

# 📍 Anchors (Position Matching)

| Symbol | Meaning |
|-----------|-------------|
| ^ | start of string |
| $ | end of string |

Example:

```python
re.findall(r"^Hello", "Hello world")
```

---

# 🎯 Groups (Capturing Data)

Parentheses capture specific parts.

```python
text = "Score: 85"

match = re.findall(r"(\d+)", text)
print(match)
```

Output:
```
['85']
```

Useful when extracting only specific pieces of text.

---

# 🧪 Practical Examples

## Extract Numbers

```python
re.findall(r"\d+", text)
```

---

## Extract Emails

```python
re.findall(r"\S+@\S+", text)
```

---

## Extract Words

```python
re.findall(r"\w+", text)
```

---

## Extract Links (basic)

```python
re.findall(r"http\S+", text)
```

---

# 🐍 Greedy vs Non-Greedy Matching ⭐ VERY IMPORTANT

## Greedy (default)

Matches as much as possible

```python
text = "<h1>Hello</h1>"

re.findall(r"<.*>", text)
```

Output:
```
['<h1>Hello</h1>']
```

❌ Captures too much

---

## Non-Greedy (Lazy)

Add `?`

```python
re.findall(r"<.*?>", text)
```

Output:
```
['<h1>', '</h1>']
```

✅ Correct behavior

---

## Rule Summary

| Type | Syntax |
|-----------|------------|
| Greedy | .* |
| Non-greedy | .*? |

👉 Always use non-greedy when parsing HTML

---

# 🧠 Raw Strings (Best Practice)

Always use raw strings:

❌ Bad
```python
"\d+"
```

✅ Good
```python
r"\d+"
```

Prevents escape character issues.

---

# 🛠️ Real World Use Cases

Regex is used for:

✅ Web scraping  
✅ Data cleaning  
✅ Log analysis  
✅ Email extraction  
✅ Form validation  
✅ API parsing  
✅ Automation scripts  
✅ Text preprocessing for AI  

---

# ⚠️ Best Practices

✅ Keep patterns simple  
✅ Test step by step  
✅ Use raw strings  
✅ Use BeautifulSoup for HTML instead of complex regex  
✅ Avoid very long unreadable patterns  

---

# 🔥 Quick Cheatsheet

```python
import re

re.search()
re.findall()
re.match()

\d+          # numbers
\w+          # words
\S+@\S+      # email
^Hello       # start match
world$       # end match
.*?          # non-greedy
```

---


# 🚀 How This Module Helps My Journey

Regex helps me:

- scrape websites
- clean API responses
- process logs
- automate tasks
- build data pipelines
- prepare for AI agents that extract information

This is a **core skill for backend development + Agentic AI systems**.

---

# ✨ Final Summary

Regular Expressions allow me to:

✔ Search  
✔ Match  
✔ Extract  
✔ Clean  
✔ Automate text  

Now I can confidently process messy real-world web data using Python.

---

## 👨‍💻 Author

Arslan  
Learning Python → Web → AI → Agentic Systems 🚀
