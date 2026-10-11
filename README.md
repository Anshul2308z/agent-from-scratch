# Agent From Scratch

A learning project that builds a command-line AI coding agent from scratch. The
agent uses OpenRouter for model responses and exposes tools for inspecting,
reading, writing, and executing files inside the `calculator` working directory.

> This project is for learning purposes. It does not include all the security
> and safety protections required for production use.

## Requirements

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/)
- An OpenRouter API key

## Setup

1. Install the dependencies:

	```bash
	uv sync
	```

2. Create a `.env` file in the project root:

	```env
	OPENROUTER_API_KEY=your_api_key_here
	```

3. Run the agent with a prompt:

	```bash
	uv run main.py "use get_file_content to read lorem.txt"
	```

	Add `--verbose` to display the prompt and token usage:

	```bash
	uv run main.py "run tests.py" --verbose
	```

## Available Tools

- `get_files_info`: Lists entries in a directory, including names, sizes, and directory status.
- `get_file_content`: Reads file contents, up to the configured character limit.
- `write_file`: Creates or overwrites a file inside the permitted working directory.
- `run_python_file`: Executes a Python file with optional command-line arguments.

The model receives these tools through `call_function_schema.py`. The working
directory is injected by `call_function.py` and is currently set to `calculator`.

## Tests

Run the individual tool checks with:

```bash
uv run test_get_files_info.py
uv run test_get_file_content.py
uv run test_write_file.py
uv run test_run_python_file.py
```


## Project Structure

```text
.
├── calculator/                # Working directory exposed to the tools
│   ├── main.py                # Example calculator CLI
│   ├── tests.py               # Calculator tests
│   └── pkg/                   # Calculator implementation modules
├── functions/                 # Tool implementations
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   └── write_file.py
├── call_function.py           # Maps model tool calls to Python functions
├── call_function_schema.py    # Tool definitions sent to the model
├── config.py                  # Runtime constants such as MAX_CHARS
├── main.py                    # CLI entry point and agent loop
├── prompts.py                 # System prompt
├── test_*.py                  # Manual checks for each tool
├── pyproject.toml             # Project metadata and dependencies
├── uv.lock                    # Locked dependency versions
└── .env                       # Local API key configuration, not committed
```
