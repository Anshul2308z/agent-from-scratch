from functions.get_files_info import get_files_info

tests = (
    {
        "wd": "calculator",
        "dir": ".",
    },
    {
        "wd": "calculator",
        "dir": "pkg",
    },
    {
        "wd": "calculator",
        "dir": "/bin",
    },
    {
        "wd": "calculator",
        "dir": "../",
    },
)

for test in tests:
    print(get_files_info(test["wd"], test["dir"]))