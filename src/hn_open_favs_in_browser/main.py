import webbrowser
import json
import sys
import os
import time


def open_in_browser(item_id):
    url = f"https://news.ycombinator.com/item?id={item_id}"
    webbrowser.open_new_tab(url)


def open_hackernews_tabs(json_file_path):
    with open(json_file_path, "r") as file:
        data = json.load(file)

    for item_id in data:
        open_in_browser(item_id)
        time.sleep(2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <relative_path_to_json_file>")
        sys.exit(1)

    relative_path = sys.argv[1]
    json_file_path = os.path.join(os.getcwd(), relative_path)

    if not os.path.exists(json_file_path):
        print(f"Error: The specified file '{json_file_path}' does not exist.")
        sys.exit(1)

    open_hackernews_tabs(json_file_path)
