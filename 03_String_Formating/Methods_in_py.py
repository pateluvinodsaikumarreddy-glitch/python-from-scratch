# Demonstrate Python string methods with examples and comments.
# Each example uses a sample string and shows how the method works.

sample = "  Hello, Python String Methods!  "
empty = ""
words = "hello world python"
letters = "abc123"

# 1. capitalize(): Capitalize first character
print(sample.capitalize())

# 2. casefold(): Case-insensitive lowercase conversion
print(sample.casefold())

# 3. center(width, fillchar): Center string in a field
print(sample.center(40, "-"))

# 4. count(sub[, start[, end]]): Count occurrences of substring
print(sample.count("o"))

# 5. encode(encoding='utf-8', errors='strict'): Convert to bytes
print(sample.encode("utf-8"))

# 6. endswith(suffix[, start[, end]]): Check if string ends with suffix
print(sample.endswith("Methods!  "))

# 7. expandtabs(tabsize=8): Replace tabs with spaces
print("a\tb\tc".expandtabs(4))

# 8. find(sub[, start[, end]]): Return lowest index of substring or -1
print(sample.find("Python"))

# 9. format(*args, **kwargs): Format using replacement fields
print("{} is fun".format("Python"))

# 10. format_map(mapping): Format using a mapping
mapping = {"lang": "Python"}
print("{lang} is fun".format_map(mapping))

# 11. index(sub[, start[, end]]): Like find() but raises ValueError if not found
print(sample.index("Python"))

# 12. isalnum(): True if all characters are alphanumeric and string not empty
print(letters.isalnum())

# 13. isalpha(): True if all characters are alphabetic and string not empty
print("Python".isalpha())

# 14. isascii(): True if all characters are ASCII
print(sample.isascii())

# 15. isdecimal(): True if all characters are decimal characters
print("123".isdecimal())

# 16. isdigit(): True if all characters are digits
print("123".isdigit())

# 17. isidentifier(): True if string is a valid Python identifier
print("my_var".isidentifier())

# 18. islower(): True if all cased characters are lowercase
print(words.islower())

# 19. isnumeric(): True if all characters are numeric
print("½".isnumeric())

# 20. isprintable(): True if string is printable or empty
print("Hello\n".isprintable())

# 21. isspace(): True if all characters are whitespace
print("   \t\n".isspace())

# 22. istitle(): True if string is titlecased
print("Hello World".istitle())

# 23. isupper(): True if all cased characters are uppercase
print("HELLO".isupper())

# 24. join(iterable): Join elements with this string as separator
print(", ".join(["apple", "banana", "cherry"]))

# 25. ljust(width[, fillchar]): Left-justify in a field
print("left".ljust(10, "."))

# 26. lower(): Convert to lowercase
print(sample.lower())

# 27. lstrip([chars]): Remove leading characters (default whitespace)
print(sample.lstrip())

# 28. maketrans(x[, y[, z]]): Create a translation table for translate()
trans = str.maketrans("aeiou", "12345")
print("apple".translate(trans))

# 29. partition(sep): Split at first occurrence of separator
print(sample.partition("Python"))

# 30. replace(old, new[, count]): Replace occurrences of substring
print(sample.replace("Python", "Coding"))

# 31. rfind(sub[, start[, end]]): Return highest index or -1
print(sample.rfind("o"))

# 32. rindex(sub[, start[, end]]): Like rfind() but raises ValueError if not found
print(sample.rindex("o"))

# 33. rjust(width[, fillchar]): Right-justify in a field
print("right".rjust(10, "."))

# 34. rpartition(sep): Split at last occurrence of separator
print(sample.rpartition("Python"))

# 35. rsplit(sep=None, maxsplit=-1): Split from the right
print(words.rsplit(" ", 1))

# 36. rstrip([chars]): Remove trailing characters (default whitespace)
print(sample.rstrip())

# 37. split(sep=None, maxsplit=-1): Split string into a list
print(words.split())

# 38. splitlines([keepends]): Split at line boundaries
print("line1\nline2".splitlines())

# 39. startswith(prefix[, start[, end]]): Check if string starts with prefix
print(sample.startswith("  Hello"))

# 40. strip([chars]): Remove leading and trailing characters
print(sample.strip())

# 41. swapcase(): Swap case of letters
print("Hello World".swapcase())

# 42. title(): Convert to title case
print("hello world".title())

# 43. translate(table): Translate characters using mapping table
print("hello".translate(str.maketrans("hlo", "HLO")))

# 44. upper(): Convert to uppercase
print(sample.upper())

# 45. zfill(width): Pad numeric string on the left with zeros
print("42".zfill(5))

# 46. __contains__(item): Support for the "in" operator
print("Python" in sample)

# 47. __len__(): Length of the string via len()
print(len(sample))

# 48. encode() with errors parameter to ignore invalid characters
print("café".encode("ascii", errors="ignore"))

# 49. format with numbered fields
print("{0} {1}".format("Hello", "World"))

# 50. format with named fields
print("{greeting}, {name}!".format(greeting="Hi", name="Alice"))
