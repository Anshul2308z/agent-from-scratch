import os

def print_results(results, directory):
    if directory == ".":
        directory = "current"
    else:
        directory = f"'{directory}'"

    output = [f"Result for {directory} directory:"]

    for result in results:
        output.append(
            f'  - {result["name"]}: file_size={result["file_size"]} bytes, is_dir={result["is_dir"]}'
        )

    return "\n".join(output)
        


def get_files_info(working_directory: str, directory: str = ".") -> str:

    try: 
        abs_working_directory = os.path.abspath(working_directory)
        target_dir = os.path.normpath(
            os.path.join(abs_working_directory, directory)
        )
        # checks weather target_dir is inside our working dir :
        valid_target_dir = os.path.commonpath(
            [abs_working_directory, target_dir]
        ) == abs_working_directory

        if valid_target_dir is False: 
            return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

        if os.path.isdir(target_dir) is False: 
            return(f'Error: "{directory}" is not a directory')

        contents = os.listdir(target_dir)
        results = []

        for content in contents:
            content_path = os.path.join(target_dir, content)
            results.append({
                "name": content,
                "file_size": os.path.getsize(content_path),
                "is_dir": os.path.isdir(content_path)
            })

        return print_results(
            results, directory
        )

        
        
    except Exception as e:
        return(f"Error:{e}")
    
# a = get_files_info(".", ".")

# print( a )

