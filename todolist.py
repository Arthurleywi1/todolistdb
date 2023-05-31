import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123$123",
    database="todo_db_list"
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

def create_todo_item(item):
    """Create a new TODO item"""
    sql = "INSERT INTO todolist (item) VALUES (%s)"
    values = (item,)
    cursor.execute(sql, values)
    db.commit()
    print("TODO item created successfully!")

def mark_todo_item_completed(todo_id):
    """Mark a TODO item as completed"""
    sql = "UPDATE todolist SET completed = 1 WHERE id = %s"
    values = (todo_id,)
    cursor.execute(sql, values)
    db.commit()
    print("TODO item marked as completed!")

def delete_todo_item(todo_id):
    """Delete a TODO item"""
    sql = "DELETE FROM todolist WHERE id = %s"
    values = (todo_id,)
    cursor.execute(sql, values)
    db.commit()
    print("TODO item deleted!")

def get_todo_list():
    """Get the list of all TODO items"""
    sql = "SELECT * FROM todolist"
    cursor.execute(sql)
    todo_list = cursor.fetchall()
    return todo_list

def print_todo_list():
    """Print the TODO list"""
    todo_list = get_todo_list()
    if not todo_list:
        print("No TODO items found.")
    else:
        print("TODO List:")
        for todo in todo_list:
            todo_id, item, completed = todo
            status = "Completed" if completed else "Pending"
            print(f"[{todo_id}] {item} - {status}")

# Main loop
while True:
    print("\nWhat would you like to do?")
    print("1. Add a task")
    print("2. Complete a task")
    print("3. Delete a task")
    print("4. Show tasks")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        item = input("Enter the task: ")
        create_todo_item(item)
    elif choice == "2":
        todo_id = input("Enter the task ID to mark as completed: ")
        mark_todo_item_completed(todo_id)
    elif choice == "3":
        todo_id = input("Enter the task ID to delete: ")
        delete_todo_item(todo_id)
    elif choice == "4":
        print_todo_list()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
cursor.close()
db.close()
