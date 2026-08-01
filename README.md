# Smart Expense Tracker API

A REST API built using **Python** and **Flask** to manage personal expenses. The API supports adding, viewing, filtering, calculating totals, and deleting expenses. Data is stored in a local JSON file without using a database.

---

## Features

- Add a new expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Delete an expense
- Store data in a local JSON file

---

## Technologies Used

- Python 3.x
- Flask
- JSON

---

## Project Structure

```
Expense-Tracker-API/
│
├── README.md
├── AI_NOTES.md
├── requirements.txt
│
├── src/
│   ├── app.py
│   ├── expense_service.py
│   ├── data.json
│   └── __init__.py
│
└── tests/
    └── test_api.py
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory

```bash
cd Expense-Tracker-API
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Server

```bash
python src/app.py
```

The server will start at

```
http://127.0.0.1:5000
```

---

## API Endpoints

### 1. Add Expense

**POST**

```
/expenses
```

Example Request

```json
{
    "title": "Pizza",
    "amount": 450,
    "category": "Food",
    "date": "2026-08-01"
}
```

---

### 2. View All Expenses

**GET**

```
/expenses
```

---

### 3. Filter Expenses by Category

**GET**

```
/expenses?category=Food
```

---

### 4. Calculate Total Expenses

**GET**

```
/expenses/total
```

Example Response

```json
{
    "total": 450
}
```

---

### 5. Delete Expense
**DELETE**

```
/expenses/<expense_id>
```
Example
```
DELETE /expenses/1
```
---
## Data Storage
The application stores all expense records in a local JSON file:
```
src/data.json
```
No external database is required.
---
## Running Tests
Run the test suite using:

```bash
pytest
```
---
## Future Improvements
- SQLite/MySQL database integration
- User authentication
- Expense update API
- Monthly expense summary
- Swagger/OpenAPI documentation
---
## Author
Developed as part of the **Diligent Software Engineering Apprenticeship 2026** take-home assignment.