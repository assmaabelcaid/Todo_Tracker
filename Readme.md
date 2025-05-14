# To-do-Tracker-App

Introducing a colorful To-do Tracking App project.
 


## What is it?

This App was programmed with Python.
It's a simple Command Line Interface (CLI) App designed to track your to-do list. 
Follow the prompts to add and complete your daily tasks.
Create, complete, update, delete, and monitor your tasks with ease. 

## How to install it?

1. Download the repository from GitHub: https://github.com/assmaabelcaid/Todo_Tracker
2. Make sure you have Python 3.11+ installed on your computer.
3. Run the command to install the required libraries:


```shell
pip install -r requirements.txt
```

## Usage:

1. Run `python todocli.py` to start the App.

2. Use --help to get suggestion on how to use the following commands:
      
   * Create a New Task: Add a new task to track (the count will start on 0).  
   * Complete Task: Mark your task as completed.  
   * Update Task: Update the Text, Category and status of your task.  
   * Delete Task: Delete the inserted task.  
   * show Tasks: show all tasks.

### Creating a New Task

* Run the application with the following command:

```shell
python todocli.py add "[Task Description]" "[Category]"
```

* Enter the name/description of your new task.
* Enter the category of your new task.
* The task will be created and stored in the database with default status "Not Completed".

### Update a Task

* Run the application with the following command:

```shell
python todocli.py update [id] "[Task Description]" "[Category]"
```
In the following order:
* Enter the id of your task.
* Enter the new name/description of your task.
* Enter the new category of your task.
* The task will be updated and stored in the database.


### Completing a Task

* Run the application with the following command:

```shell
python todocli.py complete [id]
```

* Enter the id of the task you want to complete.
* The task is now completed.

### Deleting a Task

* Run the application with the following command:

```shell
python todocli.py delete [id]
```

* Enter the id of the task you want to delete.
* The task is now completed.


### Show all Tasks

* Run the application with the following command:

```shell
python todocli.py show
```

* The complete list of your tasks will be shown.


## Note:

Note: This is a basic CLI App and it's giving purr <3.
