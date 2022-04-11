def main(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        contents = f.read()
    return contents

def test(string):
    print('hi from: ', string)