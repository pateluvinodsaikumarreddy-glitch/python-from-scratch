# Conditional Statements

## What are Conditional Statements?
Conditional statements allow a program to make decisions based on conditions. If a condition is `True`, one block of code executes; otherwise, another block may execute.

## Types
- `if` → Executes when the condition is True.
- `if...else` → Executes one block if True, another if False.
- `if...elif...else` → Checks multiple conditions; only the first True block runs.
- Nested `if` → An `if` statement inside another `if`.

## Comparison Operators
- `==` : Equal to
- `!=` : Not equal to
- `>` : Greater than
- `<` : Less than
- `>=` : Greater than or equal to
- `<=` : Less than or equal to

## Logical Operators
- `and` : All conditions must be True.
- `or` : At least one condition must be True.
- `not` : Reverses the result of a condition.

## Syntax

```python
if condition:
    # code

if condition:
    # code
else:
    # code

if condition1:
    # code
elif condition2:
    # code
else:
    # code