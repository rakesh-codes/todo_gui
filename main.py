import tkinter
from tkinter import Listbox
import tkinter.messagebox as messagebox
import db_util

class AddTask:
    def add_task(self, query):
        dbobject = db_util.Todo()
        db_connection = dbobject.getConnection()
        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()
        cursor.close()
        dbobject.closeConnection()

    def view_task(self, query):
        dbobject = db_util.Todo()
        db_connection = dbobject.getConnection()
        cursor = db_connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        dbobject.closeConnection()
        return result

add_task_instance = AddTask()


window = tkinter.Tk()
window.title("To Do")

# Function to display existing tasks
def display_task():
    listbox.delete(0, tkinter.END)  # Clear the listbox
    query = "SELECT * FROM task"
    tasks = add_task_instance.view_task(query)
    for task in tasks:
        listbox.insert(tkinter.END, task[1])  # Insert task name into listbox
        

# Function to add a task
def add_task():
    task = input_box.get()
    if len(task.strip()) == 0:
        messagebox.showinfo("Empty Task", "Please enter a task.")
    else:
        listbox.insert(tkinter.END, task)
        input_box.delete(0, tkinter.END)
        query = f"INSERT INTO task (Task_name) VALUES ('{task}')"
        add_task_instance.add_task(query)


def update_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        selected_task_name = listbox.get(selected_task_index)  # Get the selected task name from the listbox
        updated_task_name = input_box.get()  # Get the updated task name from the input box

        # Construct the SQL query to update the task name in the database
        query = f"UPDATE task SET Task_name = '{updated_task_name}' WHERE Task_name = '{selected_task_name}'"

        # Update the task name in the database
        add_task_instance.add_task(query)

        # Refresh the list of tasks displayed
        display_task()
    else:
        messagebox.showinfo("No Task Selected", "Please select a task to update.")


# Function to delete a task
def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        task_id = selected_task_index[0] + 1  # Task IDs start from 1
        query = f"DELETE FROM task WHERE id = {task_id}"
        add_task_instance.add_task(query)
        listbox.delete(selected_task_index)

# Header label
header = tkinter.Label(window, text="To Do List")
header.pack()

# Frame to hold entry box and submit button
entry_frame = tkinter.Frame(window)
entry_frame.pack()

# Entry field for adding tasks
input_box = tkinter.Entry(entry_frame, width=50)
input_box.pack(side='left')

# Button to add a task
submit_btn = tkinter.Button(entry_frame, text="Add task", command=add_task)
submit_btn.pack(side='left')
#button to update the task
update_btn = tkinter.Button(entry_frame, text="Update task", command=update_task)
update_btn.pack()

# Listbox to display tasks
listbox = Listbox(window, height=10, width=50, bg="grey", activestyle='dotbox', font="Helvetica", fg="yellow")
listbox.pack()

# Button to delete a task
delete_btn = tkinter.Button(window, text="Delete", command=delete_task)
delete_btn.pack()



# Display existing tasks when the program starts
display_task()

window.mainloop()


def update_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        task_id = selected_task_index[0] + 1  # Task IDs start from 1
        selected_task_name = listbox.get(selected_task_index)  # Get the selected task name from the listbox
        new_task_name = input_box.get()  # Get the new task name from the input box
        
        if new_task_name.strip():  # Check if the new task name is not empty
            # Construct the SQL query to update the task name in the database
            query = f"UPDATE task SET Task_name = '{new_task_name}' WHERE Task_name = '{selected_task_name}'"
            # Update the task name in the database
            add_task_instance.add_task(query)
            
            # Refresh the list of tasks displayed
            display_task()
        else:
            messagebox.showinfo("Empty Task", "Please enter a new task name.")
    else:
        messagebox.showinfo("No Task Selected", "Please select a task to update.")