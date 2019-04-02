import json
import argparse


def load_data(filepath):
    try:
        with open(filepath, encoding='utf-8') as json_file_obj:
            return json.load(json_file_obj)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return None


def get_cmdline_args():
    parser = argparse.ArgumentParser(description='JSON output in pretty form')
    parser.add_argument('json_filename', metavar='json_filename', type=str,
                        help='JSON filename')
    return parser.parse_args()


def pretty_print_json(python_object):
    return json.dumps(python_object, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    args = get_cmdline_args()
    python_object = load_data(args.json_filename)
    if python_object is None:
        exit('Input file not found or not a JSON')
    print(pretty_print_json(python_object))
