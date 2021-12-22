import os

current_path_to_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'files'))


def read_line(file_name: str):
    with open(os.path.join(current_path_to_file, file_name), 'r', encoding='utf-8') as f:
        return f.read()
