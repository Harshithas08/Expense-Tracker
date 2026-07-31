import sqlite3

# Connect to database
conn = sqlite3.connect("data.db", check_same_thread=False)
cursor = conn.cursor()

# Create table
def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        description TEXT,
        date TEXT
    )
    """)
    conn.commit()

# Insert expense
def add_expense(amount, category, description, date):
    cursor.execute("""
    INSERT INTO expenses (amount, category, description, date)
    VALUES (?, ?, ?, ?)
    """, (amount, category, description, date))
    conn.commit()

# Fetch all data
def get_expenses():
    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    return cursor.fetchall()

# Get total amount
def get_total():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    result = cursor.fetchone()[0]
    return result if result else 0
