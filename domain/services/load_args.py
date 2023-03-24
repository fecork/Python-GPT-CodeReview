import argparse


class TaskManager:
    """Class responsible for managing the tasks"""

    def __init__(self, path: str):
        self.path = path

    def run_task(self, task: str, *args):
        """Run the task specified"""
        tasks = {
            "best": self.best_practices,
            "improve": self.improve_code,
            "security": self.security_check,
            "ask": self.create_code,
            "rebuild": self.rebuild,
            "explain": self.explain_code,
            "pytest": self.pytest_run,
            "auditoria": self.audit_report,
            "tdt": self.create_code,
        }

        if task in tasks:
            tasks[task](*args)
        else:
            print("La tarea especificada no es válida")

    def best_practices(self):
        print(f"Ejecutando mejores prácticas para {self.path}")

    def improve_code(self):
        print(f"Mejorando el código de {self.path}")

    def security_check(self):
        print(f"Verificando la seguridad de {self.path}")

    def create_code(self, new):
        print(f"Creando un nuevo código para cumplir con {new}")

    def rebuild(self, error):
        print(f"Corrigiendo el error {error} en {self.path}")

    def explain_code(self):
        print(f"Explicando el código de {self.path}")

    def pytest_run(self):
        print(f"genera las pruebas unitarias usando pytest en {self.path}")

    def audit_report(self):
        print(f"genera el reporte de auditoria en {self.path}")

    def tdt(self, new):
        print(f"aplicando TDT para: {new}")


def get_args() -> argparse.Namespace:
    """Get arguments from terminal"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="El path del archivo", required=True)
    parser.add_argument(
        "-t",
        "--task",
        choices=[
            "best",
            "improve",
            "security",
            "ask",
            "rebuild",
            "explain",
            "pytest",
            "auditoria",
            "tdt",
        ],
        help="La tarea a realizar",
        required=True,
    )
    parser.add_argument(
        "-n", "--new", help="requisitos del código a crear para la tarea 'ask'"
    )
    parser.add_argument(
        "-e", "--error", help="el error que se debe corregir para la tarea 'rebuild'"
    )
    args = parser.parse_args()
    return args


def main(args):
    """Main function"""
    path = args.path
    task_manager = TaskManager(path)
    task_manager.run_task(args.task, args.new, args.error)


if __name__ == "__main__":
    args = get_args()
    main(args)
