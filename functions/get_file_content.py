import os 

def get_file_content(working_directory: str, file_path: str) -> str:

    try :
        abs_working_directory = os.path.abspath(working_directory)

        target_file = os.path.abspath(
            os.path.join(
                abs_working_directory, file_path
            )
        )

        valid_target_file = os.path.commonpath(
            [abs_working_directory, target_file]
        ) == abs_working_directory

        if valid_target_file is False: 
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if os.path.isfile(target_file) is False: 
            return f'Error: File not found or is not a regular file: "{file_path}"'

        from config import MAX_CHARS

        with open(target_file, "r") as f: 
            file_content_string = f.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if f.read(1): # empty string is falsy so if we don't have more char it's good, this if statement will not execute
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            #.read(size) continues reading from last position we read from, thus f.read(1) logic works here 

        return file_content_string
    except Exception as e:
        return f"Error: {e}"
    