# 🔄 Assignment 4 — Swap Two Numbers

A lightweight console utility built with Python that takes two numbers from the user, swaps their values in-place using Python's tuple unpacking, and outputs the swapped results.

---

## 🎮 How It Works

1. Prompts the user twice to enter two numbers via the console using `input()`.
2. Casts both inputs into integers and assigns them to variables `x` and `y`.
3. Swaps the values of `x` and `y` in a single line using tuple unpacking (`x, y = y, x`) without needing a temporary variable.
4. Displays the swapped values to the console using `print(x, y)`.

---

## 🛠️ Concepts Practised

- Reading console input with `input()`
- Type conversion from string to integer using `int()`
- Tuple packing and simultaneous variable unpacking (`a, b = b, a`)
- In-place variable value swapping without a temporary third variable
- Outputting multiple variables separated by spaces with `print()`

---

## 🏆 Example Run

```text
Enter a number: 10
Enter a number: 25
25 10
