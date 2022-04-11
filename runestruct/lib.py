import importlib.util

def import_module(task_name):
    spec = importlib.util.spec_from_file_location("module", f"tasks/{task_name}/task.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module