import typer
from rich.console import Console
from rich.table import Table

console = Console()
app = typer.Typer()

#function to add the task

@app.command(short_help='Adds an item') #short help is used to add a little help
def add(task: str, category: str): #take as input the item and the category
    typer.echo(f'Adding {task} to {category}') #typer.echo prints to the CLI

#function to delete the task

@app.command(short_help='Removes an item')
def delete(position: int):
    typer.echo(f'Deleting {position}')

#function to update the task

@app.command(short_help='Updates an item')
def update(position: int, task: str = None, category: str = None):
    typer.echo(f'Updating {position}')

#function to complete the task

@app.command(short_help='Updates an item')
def complete(position: int):
    typer.echo(f'Complete {position}')

#adding a little bit of style and color

@app.command()
def show():
    tasks = [("Todo1", "Study"), ("Todo2", "Sports")]
    console.print("[bold_magenta]Todos[/bolf magenta]!")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6, justify="center")
    table.add_column("Habit", min_width=20, justify="center")
    table.add_column("Category", min_width=12, justify="center")
    table.add_column("Completed", min_width=12, justify="center")

if __name__ == '__main__':
    app()
