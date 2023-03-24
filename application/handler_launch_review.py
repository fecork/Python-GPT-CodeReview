from infraestructure import adapter_azure_gpt


def start():
    return adapter_azure_gpt.ask_question("What is your name?")
