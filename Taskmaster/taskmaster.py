#this is a simple console-based interface for task management. Users can create tasks, view all tasks, sort tasks, search for tasks, and exit the application. It's a starting point for building a more complex web application with additional features and a user-friendly interface.


from enum import Enum
from datetime import datetime

class Priority(Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"

class Status(Enum):
    TODO = "To-Do"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

class Task:
    def __init__(self, title, description, priority, status, due_date=None, attachments=None):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.due_date = due_date
        self.attachments = attachments or []

    def __str__(self):
        return f"{self.title} - Priority: {self.priority.value}, Status: {self.status.value}"
class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, title, description, priority, status, due_date=None, attachments=None):
        task = Task(title, description, priority, status, due_date, attachments)
        self.tasks.append(task)
        return task

    def sort_tasks(self, key):
        self.tasks.sort(key=lambda x: getattr(x, key))

    def search_tasks(self, query):
        return [task for task in self.tasks if query.lower() in task.title.lower()]

    def view_all_tasks(self):
        for task in self.tasks:
            print(task)
def display_menu():
    print("\nTaskMaster Menu:")
    print("1. Create Task")
    print("2. View All Tasks")
    print("3. Sort Tasks")
    print("4. Search Tasks")
    print("0. Exit")

# Example usage:

task_manager = TaskManager()

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        priority = Priority[input("Enter priority (High/Medium/Low): ").upper()]
        status = Status[input("Enter status (To-Do/In Progress/Completed): ").upper()]
        due_date_str = input("Enter due date (YYYY-MM-DD), press Enter if none: ")
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None

        task_manager.create_task(title, description, priority, status, due_date)
        print("Task created successfully!")

    elif choice == "2":
        task_manager.view_all_tasks()

    elif choice == "3":
        key = input("Enter sorting key (title/priority/status): ")
        task_manager.sort_tasks(key)
        print("Tasks sorted successfully!")

    elif choice == "4":
        query = input("Enter search query: ")
        search_results = task_manager.search_tasks(query)
        print("\nSearch Results:")
        for result in search_results:
            print(result)

    elif choice == "0":
        print("Exiting TaskMaster. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
