import sqlite3


connection = sqlite3.connect('tgtasks.db')
cursor = connection.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS tasks "
               "(task_id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "task_name VARCHAR(500),"
               "completed BOOLEAN DEFAULT FALSE,"
               "time INTEGER)")

connection.commit()

connection.close()


def add_task(task_name: str, completed: bool = False, time: int = 0):
    taskdb = sqlite3.connect('tgtasks.db')
    task_cursor = taskdb.cursor()

    task_cursor.execute("INSERT INTO tasks (task_name, completed, time) "
                        "VALUES (?, ?, ?)",
                        (task_name, completed, time))

    taskdb.commit()
    taskdb.close()

    print(f"Task '{task_name}' added successfully.")


def complete_task(task_id: int):
    taskdb = sqlite3.connect('tgtasks.db')
    task_cursor = taskdb.cursor()

    task_cursor.execute("UPDATE tasks SET completed = ? WHERE task_id = ?",
                        (True, task_id))

    taskdb.commit()
    taskdb.close()


def get_task(task_id:int):
    taskdb = sqlite3.connect('tgtasks.db')
    task_cursor = taskdb.cursor()

    task_cursor.execute("SELECT * FROM tasks WHERE task_id = ?", (task_id,))

    taskone = task_cursor.fetchone()
    taskdb.close()

    if taskone:
        task_id, task_name, completed, time = taskone
        print(f"ID: {task_id}, Name: {task_name}, Completed: {completed}, Time: {time}")
    else:
        print(f"No task found with ID {task_id}.")


def list_tasks():
    taskdb = sqlite3.connect('tgtasks.db')
    task_cursor = taskdb.cursor()

    task_cursor.execute("SELECT * FROM tasks")
    tasks_list = task_cursor.fetchall()

    taskdb.close()
    return tasks_list

def delete_task(task_id: int):
    taskdb = sqlite3.connect('tgtasks.db')
    task_cursor = taskdb.cursor()

    task_cursor.execute("DELETE FROM tasks WHERE task_id = ?",
                        (task_id,))

    taskdb.commit()
    taskdb.close()

    print(f"Task with ID '{task_id} deleted successfully.")


def delete_all():
    taskdb = sqlite3.connect('tgtasks.db')
    task_cursor = taskdb.cursor()

    task_cursor.execute("DELETE FROM tasks")

    taskdb.commit()
    taskdb.close()

    print("All tasks have been deleted successfully")
