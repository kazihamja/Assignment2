# 🐍 Python Basics Assignment – Expression Evaluator & Text Encryption

## 📘 Description
This project contains two Python programs developed as part of a basic programming assignment:

1. **Expression Evaluator**
   - Reads mathematical expressions from a file
   - Tokenizes and parses them
   - Evaluates the result
   - Outputs tokens, parse tree, and final result

2. **Text Encryption & Decryption**
   - Encrypts text using custom shifting logic
   - Decrypts the encrypted text back to original
   - Verifies correctness of decryption

---

## ⚙️ Features

### 🔢 Expression Evaluator
- Supports operators: `+`, `-`, `*`, `/`
- Handles parentheses `()`
- Supports implicit multiplication (e.g., `2(3+4)`)
- Generates:
  - Tokens
  - Parse Tree
  - Final Result
- Error handling for invalid expressions

### 🔐 Encryption & Decryption
- Works on lowercase alphabet characters
- Uses two shift values (`s1` and `s2`)
- Two encryption rules:
  - First half letters → `#`
  - Second half letters → `$`
- Preserves non-alphabet characters
- Verifies successful decryption

---

## 📂 Files
- `evaluator.py` – Expression evaluator program  
- `encrypt_decrypt.py` – Encryption and decryption program  
- `sample_input.txt` – Input expressions for evaluator  
- `output.txt` – Evaluator results  
- `raw_text.txt` – Original text for encryption  
- `encrypted_text.txt` – Encrypted output  
- `decrypted_text.txt` – Decrypted output  
- `README.md` – Project documentation  

---

## ▶️ How to Run

### 1. Expression Evaluator
```bash
python evaluator.py
```
- Make sure `sample_input.txt` exists in the same folder
- Output will be written to `output.txt`

### 2. Encryption & Decryption
```bash
python encrypt_decrypt.py
```
- Enter values for `shift1` and `shift2` when prompted
- Input file: `raw_text.txt`
- Outputs:
  - `encrypted_text.txt`
  - `decrypted_text.txt`

---

## 💡 Example

### Expression Input
```
2(3+4)
```

### Output
```
Result: 14
```

---

## 🧠 What I Learned
- Tokenization and parsing concepts
- Expression evaluation using recursion
- File handling in Python
- String manipulation and encryption logic
- Writing structured and modular code

---

## 🚀 Future Improvements
- Support more operators (e.g., exponent `^`)
- Add GUI interface
- Improve error handling
- Support uppercase encryption
- Optimize parsing logic

---

## 👤 Author
Your Name

## 📅 Date
Add Date
