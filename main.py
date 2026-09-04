#!/usr/bin/env python3

import os
import argparse
from colorama import Fore, Back, Style

def create_paths_file():
    dir_path = os.path.expanduser("~/.config/add_to_path/")
    file_path = os.path.expanduser("~/.config/add_to_path/paths")

    if not os.path.isfile(file_path):
        os.makedirs(dir_path, exist_ok=True)
        open(file_path, "a").close() # create file


def link_in_rc_file():
    rc_paths = [
        os.path.expanduser("~/.bashrc"),
        os.path.expanduser("~/.zshrc")
    ]

    link_line = "\n# Created by add_to_path\nsource ~/.config/add_to_path/paths"

    for rc_path in rc_paths:
        if os.path.isfile(rc_path):
            with open(rc_path, "r") as file:
                content = file.read()

            if link_line not in content:
                with open(rc_path, "a") as file:
                    if content.endswith("\n"):
                        file.write(f"{link_line}\n")
                    else:
                        file.write(f"\n{link_line}\n")


def path_from_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()

    path = os.path.abspath(args.path)
    
    return path


def append_to_paths_file(path):
    paths_file_path = os.path.expanduser("~/.config/add_to_path/paths")
    
    entry = f'\nexport PATH="$PATH:{path}"'
    
    with open(paths_file_path, "r") as file:
        if entry not in file.read():
            with open(paths_file_path, "a") as file:
                file.write(entry)
                print(Style.BRIGHT + Fore.GREEN + f" Successfully added {path} to $PATH!")
        else:
            print(Style.BRIGHT + Fore.GREEN + f" {path} already in $PATH!")
    

def main():
    create_paths_file()
    link_in_rc_file()
    append_to_paths_file( path_from_arg() )


if __name__ == "__main__":
    main()
