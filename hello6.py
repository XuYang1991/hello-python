from pathlib import Path

path = Path('hello5.py')
print(path.absolute())
contents = path.read_text().rstrip()
print(contents)

path = Path('programming.txt')
path.write_text('I love programming.1111 \n')
path.write_text('I love programming.2222 \n')