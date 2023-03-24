from infraestructure.adapters import adapter_azure_gpt
from domain.services.load_parameter import load_parameters
from domain.services.load_code import load_code, save_code
from domain.services.load_args import get_args
from domain.entity.dto_promt import build_prompt

import os
from rich import console


args = get_args()
path = args.path
root_path = os.path.dirname(path)

name = os.path.basename(path)
task = args.task
new_code = args.new

error = load_code(f"{root_path}/review/best/best_{name}")
code = load_code(path)

# como seleccionar el path sin el base name

loaded_parameters = load_parameters()
parameters = loaded_parameters["open_ai_parameters_change"]
tasks = loaded_parameters["open_ai_tasks"]
task_data = build_prompt(code, error, new_code, tasks)
task_data = task_data[task]

gpt_response = adapter_azure_gpt.ask_openai(task_data["prompt"])


response = gpt_response["text"]
name = f"{task_data['nick']}{name}".replace(".py", "")

save_code(f"{root_path}/{task_data['folder']}/{task}", name, response)
console = console.Console()
colores = ["orange3", "light_salmon3", "light_pink3", "pink3", "plum3"]
console.print(response, style=colores[4])
