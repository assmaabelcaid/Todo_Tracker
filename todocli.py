import typer
from rich.console import Console
from rich.table import Table
from model import Todo
from database import get_all_todos, delete_todo, insert_todo, complete_todo, update_todo

console = Console()
app = typer.Typer()

#function to add the task

@app.command(short_help='Adds an item') #short help is used to add a little help
def add(task: str, category: str): #take as input the item and the category
    typer.echo(f'Adding {task} to {category}') #typer.echo prints to the CLI

    todo = Todo(task,category)
    insert_todo(todo)
    show()

#function to delete the task

@app.command(short_help='Removes an item')
def delete(position: int):
    typer.echo(f'Deleting {position}')
    delete_todo(position-1)
    show()

#function to update the task

@app.command(short_help='Updates an item')
def update(position: int, task: str = None, category: str = None):
    typer.echo(f'Updating {position}')
    update_todo(position-1, task, category)
    show()

#function to complete the task

@app.command(short_help='Updates an item')
def complete(position: int):
    typer.echo(f'Complete {position}')
    complete_todo(position-1)
    show()

#adding a little bit of style and color

@app.command()
def show():
    tasks = get_all_todos()
    console.print("[bold magenta]Todos[/bold magenta]!")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6, justify="center")
    table.add_column("Habit", min_width=20, justify="center")
    table.add_column("Category", min_width=12, justify="center")
    table.add_column("Completed", min_width=12, justify="center")

    def get_category_color(category):
        colors = {'Study': 'cyan', 'Sports': 'red', 'Learn': 'green'}
        if category in colors:
            return colors[category]
        return 'white'

    for idx, task in enumerate(tasks, start=1):
        c = get_category_color(task.category)
        is_done_str = 'YES' if task.status == 2 else 'NO'
        table.add_row(str(idx), task.task, f'[{c}]{task.category}[/{c}]', is_done_str)
    console.print(table)


if __name__ == '__main__':
    app()
