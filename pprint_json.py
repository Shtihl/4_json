import json
import sys


def load_data(source_filepath):
    with open(source_filepath, 'r', encoding='utf-8') as source_file:
        json_content = json.load(source_file, )
    return json_content


def pretty_print_json(data):
    pretty_json = json.dumps(data,
                             sort_keys=True,
                             indent=4,
                             ensure_ascii=False)
    print(pretty_json)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        source_file_name = sys.argv[1]
        required_content = load_data(source_file_name)
        pretty_print_json(required_content)
    else:
        print("Usage: python pprint_json.py path_to_json_file")

