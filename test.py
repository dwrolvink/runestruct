import yaml
with open('runes/test.yml', 'r', encoding='utf-8') as f:
    content = f.read()
obj = yaml.safe_load(content)

inp = obj['input']
print(inp)

tasks = obj['tasks']
for t in tasks:
    print(t['name'])