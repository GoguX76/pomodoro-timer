# Importaciones para crear consola y tabla
from rich.console import Console
from rich.table import Table


# Función que crea los componentes de la UI
def create_ui_components():
    console = Console()  # Crea la consola
    table = Table(title="Table Name")  # Crea la tabla de nombre "Table Name"
    return console, table  # Retorna ambos valores para ser usados en Timer
