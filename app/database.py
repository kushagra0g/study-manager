import sqlite3
from app.configure_files import initialize_files


def create_tables():

    # Establishing a connection with the database file
    folder_path = initialize_files()
    database = folder_path + r"\user.db"

    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        # Turning on foreign key check
        cursor.execute("""PRAGMA foreign_keys = ON;""")

        # If it is the first run, then create the tables.

        # Creating the subjects table
        cursor.execute("""
                                CREATE TABLE IF NOT EXISTS subjects(
                                    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    subject_name text UNIQUE NOT NULL
                                );
                                """)

        # Creating the tasks table
        cursor.execute("""
                                CREATE TABLE IF NOT EXISTS tasks(
                                    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    task_name text NOT NULL,
                                    task_description text,
                                    due_date TEXT,
                                    subject_id INTEGER NOT NULL,
                                    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
                                );
                                """)
    return


def add_subject(subject:str):
    # Establishing a connection with the database file
    folder_path = initialize_files()
    database = folder_path + r"\user.db"
    with sqlite3.connect(database) as connection:

        # Creating the cursor
        cursor = connection.cursor()

        # Adding the subject
        cursor.execute("""INSERT INTO subjects (subject_name)
        VALUES(?)""", (subject, ))

def add_task(task_name:str, task_description:str, due_date:str, subject:str):
    # Establishing a connection with the database file
    folder_path = initialize_files()
    database = folder_path + r"\user.db"
    try:
        with sqlite3.connect(database) as connection:

            # Creating the cursor
            cursor = connection.cursor()

            # Finding the subject ID in the subjects table
            cursor.execute("SELECT subject_id FROM subjects WHERE subject_name = (?)", (subject, ))

            result = cursor.fetchone()
            if result is None:
                raise "Subject is invalid"
            subject_id = result[0]


            # Adding the task
            cursor.execute("""INSERT INTO tasks (task_name, task_description, due_date, subject_id)
            VALUES(?, ?, ?, ?)""", (task_name, task_description, due_date, subject_id))
    except Exception as e:
        print(f"exception {e}")


def fetch_tasks(subject):
    folder_path = initialize_files()
    database = folder_path + r"\user.db"
    try:
        with sqlite3.connect(database) as connection:

            # Creating the cursor
            cursor = connection.cursor()

            # Fetching the subject_id
            cursor.execute("SELECT subject_id FROM subjects WHERE subject_name = (?)", (subject, ))
            result = cursor.fetchone()
            if result is None:
                raise "Subject is invalid"
            subject_id = result[0]

            # Fetching tasks relating with the specific subject id
            cursor.execute("SELECT * FROM tasks WHERE subject_id = (?)", (subject_id, ))
            tasks = cursor.fetchall()
            return tasks
    except Exception as e:
        print(f"exception {e}")

def fetch_all_subjects():
    folder_path = initialize_files()
    database = folder_path + r"\user.db"
    with sqlite3.connect(database) as connection:
        # Creating the cursor
        cursor = connection.cursor()

        # Fetching all subjects

        cursor.execute("SELECT subject_name FROM subjects")
        subjects = cursor.fetchall()
        return subjects

create_tables()