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


def check_shell():
    bash_path = os.path.expanduser("~/.bashrc")
    zsh_path = os.path.expanduser("~/.zshrc")
    
    if os.path.isfile(bash_path):
        return "bash"
    elif os.path.isfile(zsh_path):
        return "zsh"
    else:
        print(Style.BRIGHT + Fore.RED + f" Seems you are using shell other than ZSH or BASH. Only these two are supported :(")
        exit()


def link_in_rc_file(shell):
    bash_path = os.path.expanduser("~/.bashrc")
    zsh_path = os.path.expanduser("~/.zshrc")

    link_line = "\n# Created by add_to_path\nsource ~/.config/add_to_path/paths"

    if shell == "bash":
        with open(bash_path, "r") as file:
            content = file.read()
        
        if link_line not in content:
            with open(bash_path, "a") as file:
                if content.endswith("\n"):
                    file.write(f"{link_line}\n")
                else:
                    file.write(f"\n{link_line}\n")

    if shell == "zsh":
        with open(zsh_path, "r") as file:
            content = file.read()
        
        if link_line not in content:
            with open(zsh_path, "a") as file:
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


def source_rc_file(shell):
    if shell == "bash":
        os.system("source ~/.bashrc")
    if shell == "zsh":
        os.system("source ~/.zshrc")


def main():
    create_paths_file()
    shell = check_shell()
    link_in_rc_file(shell)
    append_to_paths_file( path_from_arg() )
    source_rc_file(shell)


if __name__ == "__main__":
    main()
