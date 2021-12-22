import ast


def from_str_to_dict(string_dict: str) -> dict:
    return ast.literal_eval(rf'{string_dict}')
