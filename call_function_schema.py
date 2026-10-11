schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists the entries in a directory relative to the working directory, including each item's name, size, and directory status. Use only when the user asks what files or directories exist. Do not use this to read file contents or execute files.",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads and returns the text content of one file relative to the working directory, truncated to 10000 characters. Use when the user asks to read, inspect, or retrieve file contents. Do not use this to list directories or execute files.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file, relative to the working directory",
                }
            },
            "required": ["file_path"],
        },
    },
}

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Creates or overwrites a file relative to the working directory with the supplied content. Use when the user asks to create, write, save, or modify a file.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Content to write to the file",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a Python file relative to the working directory and returns its output. Use when the user asks to run, execute, or test a Python file. Do not use this to inspect the file's source code.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "description": "Optional command-line arguments to pass to the Python file",
                    "items": {
                        "type": "string",
                    },
                },
            },
            "required": ["file_path"],
        },
    },
}

available_functions = [
    schema_get_files_info,
    schema_get_file_content,
    schema_write_file,
    schema_run_python_file,
]