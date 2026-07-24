# 🐍 Python Complete Course

# Section 3 - Strings

## 📖 What is a String?

A **string** is a sequence of characters enclosed in single quotes (`' '`), double quotes (`" "`), or triple quotes (`''' '''` / `""" """`).

A string can contain:
- Letters
- Numbers
- Symbols
- Spaces

### Examples

```python
name = "Vinod"
city = 'Bangalore'
message = "Hello Python"
number = "12345"
```

> **Note:** Even though `"12345"` contains numbers, it is still a **string** because it is enclosed in quotes.

---

# Why do we use Strings?

Strings are used to store textual data.

Examples:
- Names
- Email addresses
- Passwords
- Addresses
- Messages
- Phone numbers (sometimes)

Example:

```python
username = "vinod123"
email = "vinod@gmail.com"
password = "abc@123"
```

---

# Strings are Sequences

A string behaves like a **sequence of characters**.

Example:

```python
name = "VINOD"
```

| Character | V | I | N | O | D |
|-----------|---|---|---|---|---|
| Index | 0 | 1 | 2 | 3 | 4 |

Negative Indexing

| Character | V | I | N | O | D |
|-----------|---|---|---|---|---|
| Index | -5 | -4 | -3 | -2 | -1 |

---

# Indexing

Indexing is used to access individual characters.

```python
name = "VINOD"

print(name[0])
print(name[2])
print(name[-1])
```

Output

```
V
N
D
```

---

# Slicing

## Definition

Slicing means extracting a portion of a string.

### Syntax

```python
string[start:end]
```

- **start** → Included
- **end** → Excluded

Python starts from the **start index** and stops **before the end index**.

Example

```python
name = "PYTHON"

print(name[1:4])
```

Output

```
YTH
```

Because Python takes

```
Index 1 ✔
Index 2 ✔
Index 3 ✔
Index 4 ❌
```

---

### Omitting Start

```python
print(name[:4])
```

Output

```
PYTH
```

---

### Omitting End

```python
print(name[2:])
```

Output

```
THON
```

---

### Copy Entire String

```python
print(name[:])
```

Output

```
PYTHON
```

---

### Slicing with Step

Syntax

```python
string[start:end:step]
```

Example

```python
print(name[0:6:2])
```

Output

```
PTO
```

---

### Reverse a String

```python
print(name[::-1])
```

Output

```
NOHTYP
```

---

# Immutable Strings

Strings are **immutable**.

This means the original string object **cannot be modified** after it is created.

❌ Invalid

```python
name = "vinod"

name[0] = "s"
```

Output

```
TypeError
```

---

## Why does replace() work?

```python
name = "vinod"

print(name.replace("v", "s"))
```

Output

```
sinod
```

`replace()` **does not modify** the original string.

Instead, Python creates a **new string**.

```python
name = "vinod"

name = name.replace("v", "s")
```

The variable `name` now points to the new string `"sinod"`.

The original string `"vinod"` was never changed.

---

# Common String Methods

| Method | Description |
|---------|-------------|
| `upper()` | Converts to uppercase |
| `lower()` | Converts to lowercase |
| `capitalize()` | First letter uppercase |
| `title()` | First letter of every word uppercase |
| `swapcase()` | Reverses letter case |
| `replace()` | Replaces part of a string |
| `find()` | Returns index or `-1` |
| `index()` | Returns index or raises error |
| `count()` | Counts occurrences |
| `startswith()` | Checks beginning |
| `endswith()` | Checks ending |
| `strip()` | Removes spaces from both ends |
| `lstrip()` | Removes left spaces |
| `rstrip()` | Removes right spaces |
| `split()` | Converts string into list |
| `join()` | Converts list into string |
| `isalpha()` | Checks if only alphabets |
| `isdigit()` | Checks if only digits |
| `isalnum()` | Checks if only letters and digits |
| `len()` | Returns length (**built-in function**) |

---

# Common Errors

### IndexError

```python
name = "VINOD"

print(name[5])
```

Reason

```
Valid indexes are 0 to 4.
```

---

### TypeError

```python
name = "VINOD"

name[0] = "R"
```

Reason

```
Strings are immutable.
```

---

# Interview Questions

### What is a String?

A string is a sequence of characters enclosed in quotes.

---

### Are strings mutable?

No.

Strings are immutable.

---

### What is indexing?

Accessing individual characters using their position.

---

### What is slicing?

Extracting a portion of a string using indexes.

---

### Difference between find() and index()

| find() | index() |
|---------|----------|
| Returns -1 if not found | Raises ValueError |

---

### Is len() a string method?

No.

It is a built-in Python function.

---

# Summary

✔ Strings store textual data.

✔ Strings are sequences of characters.

✔ Indexing starts from `0`.

✔ Negative indexing starts from `-1`.

✔ Slicing extracts part of a string.

✔ Start index is included.

✔ End index is excluded.

✔ `[::-1]` reverses a string.

✔ Strings are immutable.

✔ String methods return a new string.

✔ `len()` is a built-in function.

---

# Folder Structure

```
Section-03-Strings/
│
├── string_basics.py
├── indexing.py
├── slicing.py
├── string_methods.py
├── immutable_strings.py
└── README.md
```

---

**Course Progress**

- ✅ Section 1 – Python Fundamentals
- ✅ Section 2 – Print(), Variables, Comments, Escape Characters, Type Casting
- ✅ Section 3 – Strings
- ⏳ Next: User Input & Operators