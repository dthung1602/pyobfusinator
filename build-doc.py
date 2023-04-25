#!/usr/bin/env python3

import os
from os.path import realpath, dirname

ROOT_DIR = realpath(dirname(__file__))
CODE_DIR = os.path.join(ROOT_DIR, "pyobfusinator")


def main():
    print("Start building doc")
    py_code = ""
    
    files = ["exception.py", "inflate.py", "compress.py"]
    for file in files:
        print(f"Combining code from {file}")
        with open(os.path.join(CODE_DIR, file)) as f:
            py_code += f.read()

    print("Replacing text")
    py_code = py_code.replace("from .exception import UnknownCharacterException", "") \
        .replace("\\", "\\\\") \
        .replace("`", "\\`")

    print("Reading HTML")
    with open(os.path.join(ROOT_DIR, "docs", "index.template.html")) as f:
        html = f.read()

    html = html.replace("__PYOBFUSINATOR_CODE_PLACEHOLDER__", py_code)

    print("Writing to index.html")
    with open(os.path.join(ROOT_DIR, "docs", "index.html"), "w") as f:
        f.write(html)


if __name__ == '__main__':
    main()
