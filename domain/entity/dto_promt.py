def validate_args(code, error, new_code):
    code = code if code else ""
    error = error if error else ""
    new_code = new_code if new_code else ""
    return code, error, new_code


def build_prompt(code: str, error: str, new_code: str, tasks) -> dict:
    print(code, error, new_code)
    code, error, new_code = validate_args(code, error, new_code)
    task_data = {
        "best": {
            "nick": "best_",
            "folder": "review",
            "prompt": f"{tasks['bad_practices']}:\n\n{tasks['best_practices']}\n\n{code}",
            "create_file": False,
        },
        "improve": {
            "nick": "improved_",
            "folder": "review",
            "prompt": f"\n\n{tasks['improve']}:\n\n{code}",
            "create_file": True,
        },
        "security": {
            "nick": "",
            "folder": "",
            "prompt": f"{tasks['security']}:\n\n{code}",
            "create_file": False,
        },
        "explain": {
            "nick": "",
            "folder": "",
            "prompt": f"{tasks['explain']}:\n\n{code}",
            "create_file": False,
        },
        "pytest": {
            "nick": "test_",
            "folder": "test",
            "prompt": f"{tasks['pytest']}:\n\n{code}",
            "create_file": True,
        },
        "ask": {
            "nick": "example_",
            "folder": "review",
            "prompt": f"{tasks['ask_favor']}:\n\n{new_code}",
            "create_file": True,
        },
        "rebuild": {
            "nick": "rebuild_",
            "folder": "review",
            "prompt": tasks["rebuild"]
            .replace("{{code}}", code)
            .replace("{{error}}", error),
            "create_file": True,
        },
        "sherlock": {
            "nick": "sherlock_",
            "folder": "",
            "prompt": f"CODE\n\n{code}\n\n{tasks['sherlock']}",
            "create_file": False,
        },
        "auditoria": {
            "nick": "auditoria_",
            "folder": "",
            "prompt": f"{tasks['auditoria']}:\n\n{code}",
            "create_file": False,
        },
    }
    return task_data
