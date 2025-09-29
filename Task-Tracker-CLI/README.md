# 📝 Task Tracker CLI

A simple **command-line interface (CLI) application** to track and manage tasks.  
You can add, update, delete, and mark tasks as `todo`, `in-progress`, or `done` — all stored locally in a JSON file.

---

## 🚀 Features
- Add new tasks with description
- Update or delete existing tasks
- Mark tasks as:
  - `todo` (default)
  - `in-progress`
  - `done`
- List tasks by status (`todo`, `in-progress`, `done`) or all
- Stores tasks in a JSON file (`tasks.json`)
- Tracks creation and update timestamps

---

## 📂 Project Structure
```
Task-Tracker-CLI/
├── task.py        # Main CLI script
├── tasks.json     # Auto-created JSON file to store tasks
└── README.md      # Project documentation
```

---

## ⚡ Usage

Run the CLI script with Python:

```bash
python3 task.py <command> [arguments...]
```

### Commands
```bash
# Add a new task
python3 task.py add "Buy groceries"

# Update a task
python3 task.py update 1 "Buy groceries and cook dinner"

# Delete a task
python3 task.py delete 1

# Mark a task as in-progress
python3 task.py mark-in-progress 1

# Mark a task as done
python3 task.py mark-done 1

# List all tasks
python3 task.py list

# List tasks by status
python3 task.py list todo
python3 task.py list in-progress
python3 task.py list done
```

---

## 🛠 Requirements
- Python **3.8+** (tested on Python 3.9 and above)
- No external dependencies (uses only built-in modules)

---

## 📌 Example
```bash
$ python3 task.py add "Finish writing report"
Task added successfully (ID: 1)

$ python3 task.py list
[1] Finish writing report - todo (Created: 2025-09-29T12:30:00, Updated: 2025-09-29T12:30:00)

$ python3 task.py mark-in-progress 1
Task 1 marked as in-progress

$ python3 task.py list in-progress
[1] Finish writing report - in-progress (Created: 2025-09-29T12:30:00, Updated: 2025-09-29T12:35:00)
```

---

## 📖 License
This project is licensed under the MIT License – feel free to use, modify, and share.
