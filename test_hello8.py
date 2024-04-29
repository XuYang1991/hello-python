from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]
path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)

person = {"first": "yang", "last": "xu"}

def test_first_name():
    assert person['first'] == 'yang'
def test_last_name():
    assert person['last'] == 'xu'

def print_person():
    print(person['first'])
    print(person['last'])
    assert person['first'] == 'yang'