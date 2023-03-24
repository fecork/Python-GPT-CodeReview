import argparse

class TaskManager:
    """
    Esta clase es responsable de administrar las tareas
    """

    def __init__(self, path):
        self.path = path

    def buenas_practicas(self):
        print(f"Ejecutando buenas prácticas para {self.path}")

    def mejorar_codigo(self):
        print(f"Mejorando el código de {self.path}")

    def verificacion_seguridad(self):
        print(f"Verificando la seguridad de {self.path}")

    def crear_codigo(self, nuevo):
        print(f"Creando un nuevo código para cumplir con {nuevo}")

    def reconstruir(self, error):
        print(f"Corrigiendo el error {error} en {self.path}")

    def explicar_codigo(self):
        print(f"Explicando el código de {self.path}")

    def ejecutar_pytest(self):
        print(f"Generando las pruebas unitarias usando pytest en {self.path}")

    def generar_reporte_auditoria(self):
        print(f"Generando el reporte de auditoría en {self.path}")


def obtener_argumentos() -> argparse.Namespace:
    """
    Esta función se encarga de obtener los argumentos
    Devuelve: args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="La ruta del archivo", required=True)
    parser.add_argument(
        "-t",
        "--tarea",
        choices=[
            "mejor",
            "mejorar",
            "seguridad",
            "solicitar",
            "reconstruir",
            "explicar",
            "pytest",
            "auditoria",
        ],
        help="La tarea a realizar",
        required=True,
    )
    parser.add_argument(
        "-n", "--nuevo", help="Requisitos del código a crear para la tarea solicitar"
    )

    parser.add_argument(
        "-e", "--error", help="El error que debe corregirse para la tarea reconstruir"
    )

    args = parser.parse_args()
    return args


def main(args):
    """
    Esta función es responsable de ejecutar las tareas principales
    Args: args

    """
    path = args.path
    task_manager = TaskManager(path)
    tarea = args.tarea
    nuevo = args.nuevo
    error = args.error

    if tarea == "mejor":
        task_manager.buenas_practicas()
    elif tarea == "mejorar":
        task_manager.mejorar_codigo()
    elif tarea == "seguridad":
        task_manager.verificacion_seguridad()
    elif tarea == "solicitar":
        task_manager.crear_codigo(nuevo)
    elif tarea == "reconstruir":
        task_manager.reconstruir(error)
    elif tarea == "explicar":
        task_manager.explicar_codigo()
    elif tarea == "pytest":
        task_manager.ejecutar_pytest()
    elif tarea == "auditoria":
        task_manager.generar_reporte_auditoria()
    else:
        print("La tarea especificada no es válida")


if __name__ == "__main__":
    args = obtener_argumentos()
    main(args)