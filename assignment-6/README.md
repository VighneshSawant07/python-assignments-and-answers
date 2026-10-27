# 🎓 Assignment 6 — Internal Assessment (IA) Result Checker

A lightweight console utility built with Python that takes the marks of two internal assessment exams (IA1 and IA2) from the user, computes their average and determines whether the student has passed or failed based on a passing threshold.

---

## 🎮 How It Works

1. Prompts the user to enter their IA1 marks and casts the input to an integer stored in variable `IA1`.
2. Prompts the user to enter their IA2 marks and casts the input to an integer stored in variable `IA2`.
3. Computes the average score using the expression `(IA1 + IA2) / 2`.
4. Evaluates whether the average is strictly greater than 10 using an `if-else` conditional statement.
5. Displays `"You have passed"` if the condition is met, otherwise displays `"You have failed"`.

---

## 🛠️ Concepts Practised

- Reading user input via the console with `input()`
- Type casting string input to integers with `int()`
- Arithmetic operators for addition (`+`) and division (`/`)
- Relational/comparison operators (`>`)
- Decision-making structures using `if` and `else` statements
- Printing conditional status messages to the screen

---

## 🏆 Example Run

**Case 1: Passed**
```text
Enter your IA1 marks: 14
Enter your IA2 marks: 12
You have passed
