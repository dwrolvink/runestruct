from yaml import safe_load
import json

def main(yaml):
    obj = safe_load(yaml)
    return json.dumps(obj)