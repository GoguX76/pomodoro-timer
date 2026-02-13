# Importaciones para la lógica del Pomodoro

import time

from rich.live import Live
from rich.progress import BarColumn, Progress, TextColumn, TimeRemainingColumn
from rich.panel import Panel
from rich.align import Align

from ui import create_ui_components, create_layout
from ascii_art import timer_ascii

# Variables del tiempo de trabajo y descanso
WORK_TIME = 1500
BREAK_TIME = 300


# Función que crea el progreso junto con la tarea para el Pomodoro
def create_progress():
    progress = Progress(TextColumn("Pomodoro"), BarColumn(), TimeRemainingColumn())
    task = progress.add_task("Trabajo", total=WORK_TIME)
    return progress, task


# Función que hace correr el Pomodoro
def run_pomodoro_timer():
    console, table, panel = create_ui_components()
    layout = create_layout()
    try:
        with Live(layout, refresh_per_second=1, console=console) as live:
            for seconds in range(WORK_TIME):
                time_left = WORK_TIME - seconds
                mins = time_left // 60
                secs = time_left % 60

                time_display = timer_ascii(mins, secs, "bold cyan")
                time_display_center = Align(time_display, align="center", vertical="middle")

                layout["timer"].update(Panel(time_display_center, title=""))

                time.sleep(1)
    except KeyboardInterrupt:
        console.print("\n\n[bold yellow]⏸️  Pomodoro detenido por el usuario[/]")
        console.print("[dim]¡Hasta pronto! 👋[/]\n")
