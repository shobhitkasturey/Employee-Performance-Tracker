

```markdown
# Employee Performance Tracker

## Overview

The Employee Performance Tracker is a command-line interface (CLI) tool designed to help track and manage employee performance. This tool allows you to add new employees, log their performance scores, and visualize their performance over time.

## Features

- **Add New Employee**: Register a new employee with their name and position.
- **Log Performance Score**: Log a performance score for an existing employee.
- **Visualize Performance**: Generate a line graph of an employee's performance over time.

## Requirements

- Python 3.x
- `pandas` library
- `matplotlib` library
- `sqlite3` library (built-in with Python)

## Installation

1. Ensure you have Python 3 installed on your machine.
2. Install the required Python libraries using pip:
    ```bash
    pip install pandas matplotlib
    ```
3. Download the `employee_performance_tracker.py` script from this repository.

## Usage

Run the script using Python from your command line:

```bash
python employee_performance_tracker.py
```

Follow the on-screen prompts to use the tool.

### Commands

1. **Add New Employee**:
    - Prompts for the employee's name and position.
    
2. **Log Performance Score**:
    - Prompts for the employee's name and performance score.

3. **Visualize Performance**:
    - Prompts for the employee's name and displays a line graph of their performance over time.

4. **Exit**:
    - Exits the tool.

## Database

The tool uses an SQLite database named `employee_performance.db` to store employee data and performance scores.

## File Structure

- `employee_performance_tracker.py`: Main script file.
- `employee_performance.db`: SQLite database file created automatically when the script is run.

## Example

Here is an example of how the tool works:

1. **Add New Employee**:
    ```plaintext
    1. Add New Employee
    2. Log Performance Score
    3. Visualize Performance
    4. Exit
    Enter your choice: 1
    Enter employee name: John Doe
    Enter employee position: Software Engineer
    Employee John Doe added successfully.
    ```

2. **Log Performance Score**:
    ```plaintext
    1. Add New Employee
    2. Log Performance Score
    3. Visualize Performance
    4. Exit
    Enter your choice: 2
    Enter employee name: John Doe
    Enter performance score: 8
    Performance score for John Doe logged successfully.
    ```

3. **Visualize Performance**:
    ```plaintext
    1. Add New Employee
    2. Log Performance Score
    3. Visualize Performance
    4. Exit
    Enter your choice: 3
    Enter employee name: John Doe
    ```
    This will display a line graph of John Doe's performance scores over time.



## Contact

For any questions or suggestions, please contact Shobhit Kasturey at shobhitkasturey@gmail.com.
```

