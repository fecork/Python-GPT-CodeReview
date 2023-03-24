import argparse

class TaskManager:
    """Clase responsable de la gestión de tareas"""

    def __init__(self, path: str):
        self.path = path
        self.tasks = {
            "best": self.best_practices,
            "improve": self.improve_code,
            "security": self.security_check,
            "ask": self.create_code,
            "rebuild": self.rebuild,
            "explain": self.explain_code,
            "pytest": self.pytest_run,
            "auditoria": self.audit_report,
        }

    def run_task(self, task: str, *args):
        """Ejecuta la tarea especificada"""
        if task in self.tasks:
            self.tasks[task](*args)
        else:
            print("La tarea especificada no es válida")

    def best_practices(self):
        """Ejecuta las mejores prácticas de codificación"""
        print(f"Ejecutando mejores prácticas para {self.path}")

    def improve_code(self):
        """Mejora el código escrito"""
        print(f"Mejorando el código de {self.path}")

    def security_check(self):
        """Realiza una verificación de seguridad"""
        print(f"Verificando la seguridad de {self.path}")

    def create_code(self, new):
        """Crea un nuevo código para cumplir con los requisitos"""
        print(f"Creando un nuevo código para cumplir con {new}")

    def rebuild(self, error):
        """Corrige un error en el código"""
        print(f"Corrigiendo el error {error} en {self.path}")

    def explain_code(self):
        """Explica el código escrito"""
        print(f"Explicando el código de {self.path}")

    def pytest_run(self):
        """Ejecuta las pruebas unitarias usando pytest"""
        print(f"genera las pruebas unitarias usando pytest en {self.path}")

    def audit_report(self):
        """Genera un informe de auditoría"""
        print(f"genera el reporte de auditoria en {self.path}")

def get_args() -> argparse.Namespace:
    """Recupera los argumentos de la línea de comandos"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="El path del archivo", required=True)
    parser.add_argument(
        "-t",
        "--task",
        choices=list(TaskManager.tasks.keys()),
        help="La tarea a realizar",
        required=True,
    )
    parser.add_argument(
        "-n", "--new", help="requisitos del código a crear para la tarea 'ask'"
    )
    parser.add_argument(
        "-e", "--error", help="el error que se debe corregir para la tarea 'rebuild'"
    )
    return parser.parse_args()

def main():
    """Función principal"""
    args = get_args()
    task_manager = TaskManager(args.path)
    task_manager.run_task(args.task, args.new, args.error)

if __name__ == "__main__":
    main()