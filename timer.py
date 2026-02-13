# Importaciones para la lógica del Pomodoro

import time

from rich.live import Live
from rich.progress import BarColumn, Progress, TextColumn, TimeRemainingColumn

from ui import create_ui_components

# Variables del tiempo de trabajo y descanso
WORK_TIME = 100
BREAK_TIME = 50


# Función que crea el progreso junto con la tarea para el Pomodoro
def create_progress():
    progress = Progress(TextColumn("Pomodoro"), BarColumn(), TimeRemainingColumn())
    task = progress.add_task("Trabajo", total=WORK_TIME)
    return progress, task


# Función que hace correr el Pomodoro
def run_pomodoro_timer():
    progress, task = create_progress()
    console, table = create_ui_components()

    with Live(progress, refresh_per_second=1, console=console) as live:
        for seconds in range(WORK_TIME):
            progress.advance(task, 1)
            time.sleep(1)
