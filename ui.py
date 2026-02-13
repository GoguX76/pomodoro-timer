# Importaciones
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.align import Align
from rich.text import Text
from ascii_art import DEVELOPMENT_ASCII

# Función que crea los componentes de la UI
def create_ui_components():
    console = Console()
    table = Table(title="Table Name")
    panel = Panel("Desarrollando", title="Panel Title")
    return console, table, panel

def create_layout():
    layout = Layout()
    ascii_art = Align.center(Text(DEVELOPMENT_ASCII, style="cyan"))

    layout.split_column(
        Layout(name="main", size=33),
        Layout(name="footer", size=3)
    )

    layout["main"].split_row(
        Layout(name="ascii_art", ratio=2),
        Layout(name="timer", ratio=2)
    )

    layout["ascii_art"].update(Panel(ascii_art, title="Desarrollo"))
    layout["timer"].update(Panel("Iniciando...", title="Tiempo"))

    layout["footer"].update(Panel("Presionea Ctrl + C para detener el Pomodoro", style="dim"))

    return layout