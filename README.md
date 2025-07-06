# 📝 Personal Journal App  
A simple command-line journal application built in Python. This app allows users to create, view, and delete personal journal entries. Entries are saved in a structured JSON file for easy access and long-term storage.

---

## ✨ Features
- Write new journal entries directly from the terminal
- View all saved entries in a clean format
- Delete specific entries by selecting them
- Saves data in a readable and structured `journal.json` file
- Modular code with `JournalEntry` class separated from app logic

---

## 📦 Requirements
- Python 3.8+
- No external libraries required (uses Python’s built-in `json` and `datetime`)

---

## 🔧 Setup

Clone the repository:
```bash
git clone git@github.com:ravneetsdeol/journal-app.git
cd journal-app

Run the app:
python3 journal.py

You’ll see a menu like:
--- Personal Journal ---
1. Write New Entry
2. View Entries
3. Exit
4. Delete Entry

## 📁 Project Structure
journal-app/
├── journal.py       # Main application
├── entry.py         # JournalEntry class
├── journal.json     # Automatically created to store your entries
├── .gitignore       # Ignores cache files and personal journal data
└── README.md        # You're reading it!

## 📜 Example Entry (Saved in JSON)
{
  "date": "2025-05-08 14:35:00",
  "title": "My First Entry",
  "body": "Today I built a Python journal app!"
}

## 🧠 Notes
The app uses list comprehensions and object serialization for saving and loading entries.
It avoids third-party libraries for simplicity and portability.
The journal file is created and maintained automatically.

## 🚀 Future Improvements
* Add search functionality by date or keyword
* Add editing capabilities for existing entries
* Encrypt or password-protect the journal
* Export entries to a Markdown or text file
