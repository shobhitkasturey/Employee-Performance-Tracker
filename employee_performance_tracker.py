
import sqlite3
from datetime import datetime
import pandas as pd

# Initialize the SQLite database
def initialize_db():
    conn = sqlite3.connect('employee_performance.db')
    c = conn.cursor()
    
    # Create tables if they do not exist
    c.execute('''CREATE TABLE IF NOT EXISTS employees (
                 id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 position TEXT NOT NULL)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS kpis (
                 id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS performance_reviews (
                 id INTEGER PRIMARY KEY,
                 employee_id INTEGER NOT NULL,
                 kpi_id INTEGER NOT NULL,
                 review_date TEXT NOT NULL,
                 score INTEGER NOT NULL,
                 FOREIGN KEY (employee_id) REFERENCES employees (id),
                 FOREIGN KEY (kpi_id) REFERENCES kpis (id))''')
    
    conn.commit()
    conn.close()

# Add an employee to the database
def add_employee(name, position):
    conn = sqlite3.connect('employee_performance.db')
    c = conn.cursor()
    c.execute('INSERT INTO employees (name, position) VALUES (?, ?)', (name, position))
    conn.commit()
    conn.close()

# Add a KPI to the database
def add_kpi(name):
    conn = sqlite3.connect('employee_performance.db')
    c = conn.cursor()
    c.execute('INSERT INTO kpis (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()

# Record a performance review
def record_performance_review(employee_id, kpi_id, review_date, score):
    conn = sqlite3.connect('employee_performance.db')
    c = conn.cursor()
    c.execute('''INSERT INTO performance_reviews (employee_id, kpi_id, review_date, score) 
                 VALUES (?, ?, ?, ?)''', (employee_id, kpi_id, review_date, score))
    conn.commit()
    conn.close()

# View employee performance
def view_employee_performance(employee_id):
    conn = sqlite3.connect('employee_performance.db')
    c = conn.cursor()
    query = '''SELECT e.name, e.position, k.name, pr.review_date, pr.score
               FROM employees e
               JOIN performance_reviews pr ON e.id = pr.employee_id
               JOIN kpis k ON pr.kpi_id = k.id
               WHERE e.id = ?'''
    c.execute(query, (employee_id,))
    records = c.fetchall()
    conn.close()
    
    if records:
        df = pd.DataFrame(records, columns=['Employee Name', 'Position', 'KPI', 'Review Date', 'Score'])
        print(df)
    else:
        print(f"No performance reviews found for employee ID {employee_id}")

# CLI for user interaction
def main():
    initialize_db()
    
    while True:
        print("1. Add Employee")
        print("2. Add KPI")
        print("3. Record Performance Review")
        print("4. View Employee Performance")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            add_employee(name, position)
            print("Employee added successfully.")
        elif choice == '2':
            kpi_name = input("Enter KPI name: ")
            add_kpi(kpi_name)
            print("KPI added successfully.")
        elif choice == '3':
            employee_id = int(input("Enter employee ID: "))
            kpi_id = int(input("Enter KPI ID: "))
            review_date = input("Enter review date (YYYY-MM-DD): ")
            score = int(input("Enter score: "))
            record_performance_review(employee_id, kpi_id, review_date, score)
            print("Performance review recorded successfully.")
        elif choice == '4':
            employee_id = int(input("Enter employee ID: "))
            view_employee_performance(employee_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
