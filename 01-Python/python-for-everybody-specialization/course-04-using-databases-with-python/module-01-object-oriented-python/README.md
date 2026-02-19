# 📘 Module — Object-Oriented Python

This module covers the fundamentals of Object-Oriented Programming (OOP) in Python.

---

# 1️⃣ OOP Definition and Terminologies

## 🔹 What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that organizes code using:

- Classes (Blueprints)
- Objects (Instances)

It models real-world entities by combining:

- Data (Attributes / Fields)
- Behavior (Methods)

---

## 🔹 Object

An object is an instance of a class.

It represents a real-world entity and contains:

- Data
- Behavior

Example:
```python
car1 = Car()
```

---

## 🔹 Object Hides Details (Encapsulation)

Objects hide internal implementation details and expose only necessary functionality.

This means:
- Internal logic is protected
- Interaction happens through public methods

This concept is called **Encapsulation**.

---

## 🔹 Interface of Objects

An interface is the set of methods and attributes used to interact with an object.

Users retrieve data or perform actions using:

```python
object.method()
```

They do NOT access internal logic directly.

---

## 🔹 Class

A class is a blueprint for creating objects.

Example:
```python
class Person:
    pass
```

---

## 🔹 Method (Message)

A method is a function defined inside a class.

Example:
```python
class Person:
    def greet(self):
        print("Hello")
```

---

## 🔹 Field / Attribute

Attributes are variables inside a class that store object data.

Example:
```python
class Person:
    def __init__(self, name):
        self.name = name
```

---

## 🔹 Object vs Instance

Object and Instance mean the same thing.

An instance is a specific object created from a class.

Example:
```python
p1 = Person("Ali")
```

---

# 2️⃣ First Class and Object

## 🔹 `class` Keyword

Used to define a class.

```python
class Student:
    pass
```

---

## 🔹 `self` Keyword

- Refers to the current instance of the class
- Must be the first parameter in instance methods

Example:
```python
class Student:
    def greet(self):
        print("Hello")
```

`self` allows access to object attributes.

---

## 🔹 Class Constructor (`__init__`)

A constructor is a special method that runs automatically when an object is created.

Example:
```python
class Student:
    def __init__(self, name):
        self.name = name
```

It is used to initialize object data.

---

## 🔹 Class Method Scope

- Variables defined with `self` belong to the object.
- Local variables inside methods cannot be accessed outside.

Example:
```python
class Test:
    def example(self):
        x = 10        # Local variable
        self.y = 20   # Object attribute
```

`x` is not accessible outside the method.  
`y` is accessible through the object.

---

## 🔹 `dir()` Function

Used to see all attributes and methods of an object.

Example:
```python
dir(object)
```

---

## 🔹 `type()` Function

Used to check the type (class) of an object.

Example:
```python
type(object)
```

---

# 3️⃣ Object Lifecycle

Objects go through three stages:

1. Creation
2. Usage
3. Destruction

---

## 🔹 Constructor

Executed when object is created.

```python
def __init__(self):
    print("Object Created")
```

---

## 🔹 Destructor (`__del__`)

Executed when object is destroyed.

```python
def __del__(self):
    print("Object Destroyed")
```

---

## 🔹 Garbage Collector

Python automatically removes objects from memory when:

- No references remain
- They are no longer in use

Memory management is automatic in Python.

---

## 🔹 Many Instances

Multiple objects can be created from one class.

Each object has its own independent data.

Example:
```python
s1 = Student("Ali")
s2 = Student("Ahmed")
```

---

## 🔹 Constructor Parameters

Constructors can accept parameters to initialize object attributes.

Example:
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

# 4️⃣ Inheritance

Inheritance allows one class to reuse properties and methods of another class.

---

## 🔹 DRY Principle

DRY = Don't Repeat Yourself.

Inheritance helps avoid duplicate code.

---

## 🔹 Base Class (Parent Class)

The class being inherited from.

Example:
```python
class Animal:
    def speak(self):
        print("Sound")
```

---

## 🔹 Child Class

The class that inherits from another class.

Example:
```python
class Dog(Animal):
    pass
```

Dog inherits the `speak()` method from Animal.

---

## 🔹 `super()` Function

Used to call methods from the parent (base) class.

Example:
```python
class Dog(Animal):
    def __init__(self):
        super().__init__()
```

`super()` allows access to parent class functionality.

---

# 📌 Module Summary

In this module, you learned:

- OOP concepts and terminology
- Classes and objects
- Encapsulation and interfaces
- `self` keyword
- Constructors and destructors
- Object lifecycle
- Garbage collection
- Multiple instances
- Inheritance
- DRY principle
- `super()` function

This forms the foundation of backend development and scalable software design.

## 👨‍💻 Author

Arslan  
Learning Python → Web → Databases → AI → Agentic Systems 🚀