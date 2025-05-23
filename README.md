# Data-Format

This Python script neatly formats an item name and its price to display them in a consistent style using **dot (`.`) padding** — similar to what you see on receipts or menus.

## 💡 What It Does

- Prompts the user to enter:
  - An item name (string)
  - Its price (string or number)
- Automatically aligns the item name and the price in one line.
- Fills the space between the name and price with dots (`.`) for better readability.

## 📁 File

- `data-format.py`: Script that formats and prints the result.

## 🧠 Logic

- Uses the `ljust()` method to left-justify the item name.
- Dynamically adjusts the padding based on the price length so the total line length remains consistent (25 characters by default).

## ▶️ How to Run

```bash
python data-format.py


