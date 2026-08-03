# 🐍 Python Basics - `print()` Function

The `print()` function is used to display output on the screen.

---

# 📌 Syntax

```python
print(object)
```

### Example

```python
print("Hello")
```

**Output**

```
Hello
```

---

# 📌 Printing Different Values

## 1️⃣ Print Text

```python
print("Python")
```

**Output**

```
Python
```

---

## 2️⃣ Print Numbers

```python
print(100)
```

**Output**

```
100
```

---

## 3️⃣ Print Variables

```python
name = "Vinod"

print(name)
```

**Output**

```
Vinod
```

---

## 4️⃣ Print Multiple Values

```python
name = "Vinod"
age = 23

print(name, age)
```

**Output**

```
Vinod 23
```

💡 **Note**

Python automatically inserts a **space** between multiple values.

Equivalent to:

```python
print(name, age, sep=" ")
```

---

# 📌 `sep` Parameter

## What is `sep`?

`sep` means **Separator**.

It tells Python **what should appear between multiple values**.

### Default Value

```python
sep = " "
```

(Default = One Space)

---

## Example 1

```python
print("Java", "Python", "C")
```

Output

```
Java Python C
```

---

## Example 2

```python
print("Java", "Python", sep="-")
```

Output

```
Java-Python
```

---

## Example 3

```python
print(10, 20, 30, sep=" | ")
```

Output

```
10 | 20 | 30
```

---

## Example 4

```python
print("A", "B", "C", sep="***")
```

Output

```
A***B***C
```

---

# 📌 Delimiter

A **delimiter** is simply a character used to separate values.

| Data | Delimiter |
|------|-----------|
| Apple,Banana,Mango | `,` |
| Java\|Python\|C++ | `\|` |
| A-B-C | `-` |

In Python, the delimiter is controlled using **`sep`**.

Example

```python
print("Apple", "Banana", "Mango", sep=",")
```

Output

```
Apple,Banana,Mango
```

---

# 📌 `end` Parameter

## What is `end`?

`end` decides **what comes after a print statement finishes.**

### Default Value

```python
end="\n"
```

(`\n` means New Line)

---

## Default Behaviour

```python
print("Hello")
print("World")
```

Output

```
Hello
World
```

Python automatically does this:

```
Hello\n
World
```

---

## Changing `end`

```python
print("Hello", end=" ")
print("World")
```

Output

```
Hello World
```

---

Another Example

```python
print("Python", end=" -> ")
print("Java")
```

Output

```
Python -> Java
```

---

# 📌 `sep` vs `end`

| `sep` | `end` |
|--------|--------|
| Works **between** values | Works **after** the print statement |
| Used inside one `print()` | Executes after the entire `print()` |
| Default = `" "` | Default = `"\n"` |

### Example

```python
print("A", "B", sep="-", end=" ")
print("C")
```

Output

```
A-B C
```

### How Python Executes

```
A
 ↓
sep="-"
 ↓
B
 ↓
end=" "
 ↓
Next print()
```

Final Output

```
A-B C
```

---

# 📌 Single Quotes vs Double Quotes

Both create **strings**.

```python
print("Python")
```

```python
print('Python')
```

Output

```
Python
```

---

## ✅ Use Double Quotes

When your string contains an apostrophe (`'`).

```python
print("I'm Vinod")
```

Output

```
I'm Vinod
```

---

## ✅ Use Single Quotes

When your string contains double quotes.

```python
print('He said "Hello"')
```

Output

```
He said "Hello"
```

---

## ❌ Wrong Example

```python
print('I'm Vinod')
```

Python reads it like this:

```
'I'
m Vinod'
```

So it throws a **SyntaxError**.

---

# 📌 Quick Summary

| Concept | Purpose | Default |
|---------|----------|----------|
| `print()` | Displays output | — |
| `sep` | Separator between values | `" "` |
| `end` | What comes after printing | `"\n"` |
| `' '` | Single quotes for strings | — |
| `" "` | Double quotes for strings | — |

---

# 💻 Practice

### Exercise 1

Print

```
Java-Python-C++
```

using

```python
sep="-"
```

---

### Exercise 2

Print

```
1 | 2 | 3 | 4 | 5
```

---

### Exercise 3

Print

```
Hello -> Python
```

using

```python
end=
```

---

### Exercise 4

Print

```
I'm learning Python
```

without getting a syntax error.

---

# 🎯 Remember

✅ `print()` → Displays output

✅ `sep` → **Between** values

```
A-B-C
```

✅ `end` → **After** printing

```
Hello World
```

✅ `' '` and `" "` both create strings.

Choose one style and use it consistently.