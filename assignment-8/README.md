# ❗ Assignment 8 — Factorial of a Number

A lightweight console utility built with Python that takes a number from the user, calculates its factorial using an iterative `for` loop, and outputs the result.

---

## 📝 Assignment Question

**Calculate factorial of a number.**

---

## 🎮 How It Works

1. Prompts the user with `"Enter number to find its factorial : "` via the console.
2. Reads the input and casts it into an integer stored in variable `num`.
3. Initializes an accumulator variable `fact` to `1`.
4. Uses a `for` loop across the range from `2` up to `num + 1`, multiplying `fact` iteratively by each value of `i` (`fact *= i`).
5. Converts `fact` to a string using `str()` and concatenates it to display the final result with `print()`.

---

## 🛠️ Concepts Practised

- Reading console input with `input()`
- Type conversion between strings and integers using `int()` and `str()`
- Iterative looping using `for` and the `range()` function
- In-place compound assignment operators (`*=`)
- String concatenation using the `+` operator

---

## 🏆 Example Run

```text
Enter number to find its factorial : 5
The factorial of the given number is 120
