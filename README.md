# 🤖 Automata Theory Project – Drawing Robot with Python

**KTU COM2022 project built with Lex & Yacc and Regular Expressions**  
A Python-based drawing robot that interprets commands and visualizes them using Turtle Graphics.

---

## 🎯 Project Purpose

This project allows users to process randomly selected lines from a `.txt` file, tokenize them using **Lex/Yacc (PLY)**, and **draw corresponding shapes** using the **Turtle graphics** module in Python.

It provides a visual and interactive way to reinforce programming fundamentals and explore:

- Tokenization (Lexing)
- Command parsing
- Graphics rendering
- GUI design
- EPS → PNG conversion with Ghostscript

---

## 🧠 How It Works

### 1. 📄 User Input & Random Line Selection
- The user is prompted to enter the name of a text file.
- The file is read and **one random line** is selected.

### 2. 🧪 Lexical Analysis (PLY Lexer)
- The selected line is tokenized using `ply.lex`.
- The output tokens are saved to:
  - `b.txt` (raw token output)
  - A Python list (used internally)

### 3. 🐢 Drawing with Turtle
- Tokens are interpreted as drawing instructions:
  - Example: forward, turn, loop
- The drawing is visualized using `turtle` and saved as `.eps`.
- EPS is converted to PNG using **Ghostscript**.

### 4. 🖼️ GUI with Tkinter
- **Stage 1:** User enters the file name.
- **Stage 2:** Shows the drawing result and error messages (e.g., mismatched parentheses).

---

## ⚙️ Technologies Used

- `Python`
- `ply` – Lex & Yacc in Python
- `tkinter` – GUI Interface
- `turtle` – Drawing module
- `Ghostscript` – EPS to PNG conversion
- `random`, `os`, `sys` – Standard utilities

---

## 📦 Project Structure

```
Automata-Theory-Project/
├── lexer.py                 # Tokenizer (PLY)
├── draw.py                  # Turtle drawing logic
├── gui.py                   # GUI using tkinter
├── convert.py               # EPS to PNG conversion
├── b.txt                    # Token output file
├── sample.txt               # Example input file
└── main.py                  # Entry point
```

---

## ▶️ How to Run

1. Install Ghostscript if not already installed.
2. Run the main Python file:

```bash
python main.py
```

3. Enter the name of a `.txt` file (e.g., `sample.txt`).
4. View the resulting drawing and possible errors in the GUI.

---

## 📸 Output Format

- 🖼️ EPS files: Vector output of the drawing
- 📷 PNG files: Converted images for display
- 💾 `b.txt`: Stores list of tokens from lexer

---

## 🎯 Project Goals

- Provide hands-on practice with:
  - Lexical analysis
  - Drawing automation
  - File handling and parsing
- Strengthen understanding of:
  - Modular Python development
  - GUI applications
  - Turtle-based drawing logic

---

## 📝 License

This project is part of KTU COM2022 coursework and is shared for educational use.

---

📐 **Code the command. See it drawn. Learn by doing.**
