import sys
import yaml

from .lib import import_module
from .ledger import Ledger

class Engine:
    ledger = None
    
    def __init__(self):
        self.ledger = Ledger()

    def run_rune(self, rune_path):
        # Open rune code
        with open(rune_path, 'r', encoding='utf-8') as f:
            content = f.read()
            rune = yaml.safe_load(content)

        # Run tasks
        for t in rune['tasks']:
            self.run_rune_task(t, rune)

    def run_rune_task(self, task, rune):
        # shorthand
        ledger = self.ledger
        rune_input = rune['input']

        print(task['name'])
        
        # get input
        inputs = self.get_inputs(task, rune_input)

        try:
            # import task code
            module = import_module(task['name'])

            # Run main()
            output = module.main(*inputs)

            # set output
            ledger.set(task['output'], output) 

            print(ledger.get(task['output']))
            print('--------------------------')

        except Exception as e:
            print('catched in engine:', e)
            raise e

    def get_inputs(self, task, rune_input):
        # shorthand
        ledger = self.ledger

        # Init        
        inputs = []

        # compile inputs
        if isinstance(task['input'], str):
            if task['input'] in rune_input.keys():
                inputs.append(rune_input[task['input']])

            elif task['input'] in ledger.keys():
                inputs.append(ledger.get(task['input']))
            else:
                raise Exception(f"Input {task['input']} to task {task['name']} was not set.")
        else:
            # [todo] implement
            raise Exception('error: multiple inputs not yet implemented')

        return inputs