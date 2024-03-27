import sqlite3

class Database:
    def __init__(self) -> None:
        """Creating a connection with database and creating table with cursor"""
        
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
        self.creating_table()

    def creating_table(self):
        """Creating a table for tasks"""

        self.cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id integer PRIMARY KEY AUTOINCREMENT, task_create varchar(50) NOT NULL, data varchar(50), completed BOOLEAN NOT NULL CHECK (completed IN (0, 1)))")
        self.connection.commit()

    def creating_task(self, task_create, data=None):
        """Creating a task with default parametrs"""

        self.cursor.execute("INSERT INTO tasks(task_create, data, completed) VALUES(?, ?, ?)", (task_create, data, 0))
        self.connection.commit()
        self.cursor.execute("SELECT id, task_create, date FROM tasks WHERE task_create = ? and completed = 0", (task_create,))
        created_task = self.cursor.fetchall()
        return created_task

    def get_task(self):
        """Get information about a completed/uncompleted tasks"""

        completed_task = self.cursor.execute("SELECT id, task_create, data FROM tasks WHERE and completed = 1").fetchall()
        uncompleted_task = self.cursor.execute("SELECT id, task_create, data FROM tasks WHERE and completed = 0").fetchall()
        return completed_task, uncompleted_task
    
    def mark_as_completed(self, task_id):
        """Mark task as completed"""

        self.cursor.execute("UPDATE tesks SET completed=1 WHERE id=?", (task_id,))
        self.connection.commit()

    def mark_uncompleted(self, task_id):
        """Mark task as uncompleted"""

        self.cursor.execute("UPDATE tesks SET completed=0 WHERE id=?", (task_id,))
        self.connection.commit()
    
    def close_connection(self):
        """Close the connection with database"""
        self.connection.close()