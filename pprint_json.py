import json
import argparse


def load_data(filepath):
    try:
        with open(filepath, encoding='utf-8') as json_file_obj:
            return json.load(json_file_obj)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return None


def gen_indent(indent_level):
    return '    ' * indent_level


def gen_print_json_array(json_data, open_char, close_char, indent_level):
    indent = gen_indent(indent_level)
    last_indent = gen_indent(indent_level - 1)
    out_list = []
    for json_elem in json_data:
        string = '\n' + indent + pretty_print_json(json_elem, indent_level + 1)
        out_list.append(string)
    return open_char + ','.join(out_list) + '\n' + last_indent + close_char


def pretty_print_json_list(json_data, indent_level):
    return gen_print_json_array(json_data, '[', ']', indent_level)


def pretty_print_json_dict(json_data, indent_level):
    return gen_print_json_array(json_data.items(), '{', '}', indent_level)


def pretty_print_json_tuple(json_data, indent_level):
    key, value = json_data
    return '"' + key + '": ' + pretty_print_json(value, indent_level)


def pretty_print_json_number(json_data, indent_level):
    return str(json_data)


def pretty_print_json_string(json_data, indent_level):
    return '"' + json_data + '"'


def pretty_print_json_bool(json_data, indent_level):
    # a little bit of a bollywood magic
    return str(json_data).lower()


def pretty_print_json_null(json_data, indent_level):
    return 'null'


# имхо вариант с ифами поудачнее :( но бот не пропустил
# https://github.com/cr00z/4_json/blob/7ebe4254b901e66fb3eb18f07ebbe8dbb08fadd4/pprint_json.py
def pretty_print_json(json_data, indent_level=1):
    return {
        type(json_data) is list: pretty_print_json_list,
        type(json_data) is dict: pretty_print_json_dict,
        type(json_data) is tuple: pretty_print_json_tuple,
        type(json_data) is int or
        type(json_data) is float: pretty_print_json_number,
        type(json_data) is str: pretty_print_json_string,
        type(json_data) is bool: pretty_print_json_bool,
        json_data is None: pretty_print_json_null
    }[True](json_data, indent_level)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='JSON output in pretty form')
    parser.add_argument('json_filename', metavar='json_filename', type=str,
                        help='JSON filename')
    args = parser.parse_args()
    dirty_json = load_data(args.json_filename)
    if dirty_json is None:
        exit('Input file not found or not a JSON')
    print(pretty_print_json(dirty_json))
