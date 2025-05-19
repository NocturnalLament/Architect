# Command Line Tool

A simple command-line interface tool with various utilities.

## Usage

The tool provides several commands that you can use:

### Hello Command
Say hello to someone:
```bash
python cli.py hello [NAME]
```

Example:
```bash
python cli.py hello John
```

### Count Command
Count up to a specified number:
```bash
python cli.py count [NUMBER]
```

Example:
```bash
python cli.py count 5
```

### Make Folder Command
Create a new folder:
```bash
python cli.py make-folder --name [FOLDER_NAME]
```

Example:
```bash
python cli.py make-folder --name my_new_folder
```

### Make File Command
Create a new file with content:
```bash
python cli.py make-file --name [FILE_NAME] --content [CONTENT]
```

Example:
```bash
python cli.py make-file --name test.txt --content "Hello, World!"
```

The content is optional. To create an empty file:
```bash
python cli.py make-file --name empty.txt
```

### Remove File Command
Remove a file:
```bash
python cli.py remove-file --name [FILE_NAME]
```

Example:
```bash
python cli.py remove-file --name test.txt
```

### Remove Folder Command
Remove a folder and all its contents recursively:
```bash
python cli.py remove-folder --name [FOLDER_NAME]
```

Example:
```bash
python cli.py remove-folder --name my_new_folder
```

**Note**: This command will remove the folder and ALL its contents recursively. Use with caution!

### Help
To see all available commands and their descriptions:
```bash
python cli.py --help
```

To see help for a specific command:
```bash
python cli.py hello --help
python cli.py count --help
python cli.py make-folder --help
python cli.py make-file --help
python cli.py remove-file --help
python cli.py remove-folder --help
``` 