import sqlite3
##datetime timestamp


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

#add_task("Finish the report", completed=False, time=120)


def list_tasks():
    taskdb = sqlite3.connect('tgtasks.db')
    task_cursor = taskdb.cursor()

    task_cursor.execute("SELECT * FROM tasks")
    tasks_list = task_cursor.fetchall()

    taskdb.close()
    return tasks_list

    # if tasks_list:
    #     result = " "
    #     print("Tasks in the database:")
    #     for task in tasks_list:
    #         task_id, task_name, completed, time = task
    #         result = f"ID: '{task_id}', Name: '{task_name}', Completed: '{completed}', Time: '{time}'"
    #         print(result)
    #     else:
    #         result = "No more tasks found."
    #     return result


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


# add_task("Finish the report", completed=False, time=120)
# get_task(1)

# async def add_to_database(telegram_id, username):
#     async with sqlite3.connect('tg.db') as db:
#         await db.execute("CREATE TABLE IF NOT EXISTS users "
#                          "(telegram_id BIGINT, "
#                          "username VARCHAR(255))")
#         cursor = await db.execute("SELECT * FROM users WHERE telegram_id = ?",
#                                   (telegram_id,))
#         data = await cursor.fetchone()
#         if data is not None:
#             return
#     async with sqlite3.connect('tg.db') as db:
#         await db.execute("INSERT INTO users (telegram_id, username) VALUES (?, ?)",
#                          (telegram_id, username))
#         await db.commit()


# async def add_task_to_database(task_name):
#     async with sqlite3.connect('tgtasks.db') as taskdb:
#         await taskdb.execute("CREATE TABLE IF NOT EXISTS tasks ("
#                              "task_id INTEGER PRIMARY KEY AUTOINCREMENT,"
#                              "task_name VARCHAR(500),"
#                              "completed BOOLEAN DEFAULT FALSE,"
#                              "time INTEGER ")
#         await taskdb.commit()
#         cursor = await taskdb.execute("SELECT * FROM tasks WHERE task_name = ?",
#                                       (task_name,))
#         async with sqlite3.connect('tgtasks.db') as taskdb:
#             data = await cursor.fetchone()
#
#             await taskdb.execute("INSERT INTO tasks (task_id, task_name, completed) VALUES (?, ?, ?)",
#                                  task_name)
#             await taskdb.commit()
#
#         async with sqlite3.connect('tgtasks.db') as taskdb:
#             cursor = await taskdb.execute("SELECT * FROM tasks WHERE task_name = ?",
#                                           (task_name,))
#             data = await cursor.fetchone()
#             print(data)