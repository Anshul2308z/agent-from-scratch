import os 

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:

    try: 
        abs_working_directory = os.path.abspath(
            working_directory
        )
        #target file is absolute path 
        target_file = os.path.abspath(
            os.path.join(
                abs_working_directory, file_path
            )
        )
        valid_target_file = os.path.commonpath(
            [abs_working_directory, target_file]
        ) == abs_working_directory

        if valid_target_file is False: 
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if os.path.isfile( target_file ) is False: 
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if target_file.endswith(".py") is False: 
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]
        if args: 
            command.extend(args)

        import subprocess


        result = subprocess.run(command, 
            timeout=30, 
            cwd=abs_working_directory, 
            capture_output=True, 
            text=True)

        #print( result)
        #CompletedProcess(args=['python', '/home/anshul/Documents/Learnings/bootdev-agent/main.py'], returncode=2, stdout='', stderr='usage: main.py [-h] [--verbose] prompt\nmain.py: error: the following arguments are required: prompt\n')

        output_string = ""

        if result.returncode != 0 :
            output_string += f"Process exited with code {result.returncode}"
        if result.stdout is None or result.stderr is None:
            output_string += "\nNo output produced"
        else: 
            output_string += f"\nSTDOUT: {result.stdout}"
            output_string += f"\nSTDERR: {result.stderr}"

        return output_string
    except Exception as e:
        return f"Error: {e}"
