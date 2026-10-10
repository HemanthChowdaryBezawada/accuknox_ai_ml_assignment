# AccuKnox AI/ML Trainee Assessment

**Candidate:** Bezawada Hemanth Chowdary

This repository contains the solutions for the Python and database programming tasks in the AccuKnox AI/ML Trainee assessment.

The Links to the task 4 and 5 of Problem statement 1 are added at the end of this document

## Problem Statement 1

### Task 1: API Data Retrieval and SQLite Storage

**Files:** `fetch_books.py`, `store_books.py`

- Retrieves book information from the Open Library Search API.
- Extracts the book title, author, first publication year, and language.
- Stores the selected information in a local SQLite database.
- Retrieves and displays the stored book records.

**API:** https://openlibrary.org/search.json?q=science+fiction&limit=10

**Technologies:** Python, Requests, SQLite.

**Assumption:** The search is limited to 10 results for a simple demonstration. Multiple authors and languages are stored as comma-separated text.

### Task 2: Student Score Processing and Visualization

**File:** `student_scores.py`

- Retrieves student performance data from an external HTTP endpoint.
- Parses the CSV response using Python's built-in CSV module.
- Extracts the final grade (`G3`) for each returned student record.
- Calculates and prints the average final grade.
- Creates a bar chart using Matplotlib.

**API:** https://api.datapoint.market/r/data37/student-performance

**Technologies:** Python, Requests, CSV, Matplotlib.

**Assumption:** The average is calculated from the records returned by the endpoint. The result represents those retrieved records, not necessarily every student in the original dataset.

### Task 3: CSV Import into SQLite

**Files:** `import_users.py`, `users.csv`

- Reads user information from a CSV file.
- Creates a local SQLite database and a `users` table if needed.
- Inserts names and email addresses using parameterized SQL statements.
- Uses a unique constraint on the email column to prevent duplicate email values.

**Technologies:** Python, CSV, SQLite.

**Assumption:** The input CSV contains `name` and `email` columns. The sample file uses fictional user information.

## Requirements

- Python 3
- Requests
- Matplotlib

Install the external dependencies for the relevant task:

```bash
python3 -m pip install requests matplotlib
```

The `csv`, `sqlite3`, and `io` modules used in these scripts are included in Python's standard library.

## How to Run

Run each script from its own task directory.

**Task 1**

```bash
cd problem_statement_1/task1_api_to_sqlite
python3 fetch_books.py
python3 store_books.py
```

**Task 2**

```bash
cd problem_statement_1/task2_student_scores
python3 student_scores.py
```

A Matplotlib chart should appear after the average grade is calculated.

**Task 3**

```bash
cd problem_statement_1/task3_csv_to_sqlite
python3 import_users.py
```

Ensure `users.csv` is present in the Task 3 directory before running the script.

The scripts create their SQLite database files locally when executed.

## Additional Projects

### Most Complex Python Code

https://github.com/HemanthChowdaryBezawada/geospatial-measurement-api

### Most Complex Database Code

https://github.com/HemanthChowdaryBezawada/Storyscape_app/blob/main/backend/schema.sql

