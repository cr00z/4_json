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


def gen_print_json_lst(dataset, open_char, close_char, indent_level):
    indent = gen_indent(indent_level)
    last_indent = gen_indent(indent_level - 1)
    out_list = []
    for item in dataset:
        string = '\n' + indent + pretty_print_json(item, indent_level + 1)
        out_list.append(string)
    return open_char + ','.join(out_list) + '\n' + last_indent + close_char


def pretty_print_json(json_data, indent_level=1):
    if type(json_data) is list:
        return gen_print_json_lst(iter(json_data), '[', ']', indent_level)
    elif type(json_data) is dict:
        return gen_print_json_lst(json_data.items(), '{', '}', indent_level)
    elif type(json_data) is tuple:
        key, value = json_data
        return '"' + key + '": ' + pretty_print_json(value, indent_level)
    elif type(json_data) is int or type(json_data) is float:
        return str(json_data)
    elif type(json_data) is str:
        return '"' + json_data + '"'
    elif type(json_data) is bool:
        # a little bit of a bollywood
        return str(json_data).lower()
    elif json_data is None:
        return 'null'
    return ''


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='JSON output in pretty form')
    parser.add_argument('json_filename', metavar='json_filename', type=str,
                        help='JSON filename')
    args = parser.parse_args()
    dirty_json = load_data(args.json_filename)
    if dirty_json is None:
        exit('Input file not found or not a JSON')
    print(pretty_print_json(dirty_json))
