#!/usr/bin/env python3

import argparse
import sys
import os
import shutil
from randfacts import get_fact
import wikipedia
import joke

def create_parser():
    """Create the command line parser."""
    parser = argparse.ArgumentParser(
        description="Command line tool for various operations",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Example command: hello
    hello_parser = subparsers.add_parser('hello', help='Say hello to someone')
    hello_parser.add_argument('name', help='Name of the person to greet')
    
    # Example command: count
    count_parser = subparsers.add_parser('count', help='Count up to a number')
    count_parser.add_argument('number', type=int, help='Number to count to')
    
    # Command: make-folder
    folder_parser = subparsers.add_parser('make-folder', help='Create a new folder')
    folder_parser.add_argument('--name', dest='folder_name', required=True, help='Name of the folder to create')
    
    # Command: make-file
    file_parser = subparsers.add_parser('make-file', help='Create a new file with content')
    file_parser.add_argument('--name', dest='file_name', required=True, help='Name of the file to create')
    file_parser.add_argument('--content', help='Content to write to the file', default='')

    remove_file = subparsers.add_parser('remove-file', help='Remove a file')
    remove_file.add_argument('--name', dest='file_name', required=True, help='Name of the file to remove')

    remove_folder = subparsers.add_parser('remove-folder', help='Remove a folder')
    remove_folder.add_argument('--name', dest='folder_name', required=True, help='Name of the folder to remove')

    random_fact = subparsers.add_parser("random-fact", help="Get a random fact")
    random_fact.add_argument('--inappropriate', help="Get an inappropriate fact", action='store_true')

    wiki = subparsers.add_parser("wiki", help="Get a wiki summary")
    wiki.add_argument('--search', help="Search for a wiki summary", required=True)
  
    return parser

def hello_command(args):
    """Handle the hello command."""
    print(f"Hello, {args.name}!")

def count_command(args):
    """Handle the count command."""
    for i in range(1, args.number + 1):
        print(i)

def make_folder_command(args):
    """Handle the make-folder command."""
    os.makedirs(args.folder_name, exist_ok=True)
    print(f"Folder '{args.folder_name}' created successfully.")

def make_file_command(args):
    """Handle the make-file command."""
    with open(args.file_name, 'w') as f:
        if args.content:
            f.write(args.content)
    print(f"File '{args.file_name}' created successfully.")

def remove_file_command(args):
    """Handle the remove-file command."""
    os.remove(args.file_name)
    print(f"File '{args.file_name}' removed successfully.")

def remove_folder_command(args):
    """Handle the remove-folder command."""
    try:
        shutil.rmtree(args.folder_name)
        print(f"Folder '{args.folder_name}' and all its contents removed successfully.")
    except FileNotFoundError:
        print(f"Error: Folder '{args.folder_name}' not found.")
    except Exception as e:
        print(f"Error removing folder: {str(e)}")

def random_fact_command(args):
    """Handle the random-fact command."""
    # args.inappropriate will be True if --inappropriate was provided, False otherwise
    is_inappropriate = args.inappropriate  # This is a raw boolean
    print(get_fact(is_inappropriate))

def get_wiki(args):
    """Handle the wiki command."""
    result = wikipedia.summary(args.search, sentences=5)
    return result




def main():
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args()
    
    if args.command == 'hello':
        hello_command(args)
    elif args.command == 'count':
        count_command(args)
    elif args.command == 'make-folder':
        make_folder_command(args)
    elif args.command == 'make-file':
        make_file_command(args)
    elif args.command == 'remove-file':
        remove_file_command(args)
    elif args.command == 'remove-folder':
        remove_folder_command(args)
    elif args.command == 'random-fact':
        random_fact_command(args)
    elif args.command == 'wiki':
        print(get_wiki(args))

    else:
        parser.print_help()
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main()) 