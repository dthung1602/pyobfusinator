import sys
from argparse import ArgumentParser

from .compress import unicode_compress
from .inflate import inflate


def main():
    parser = ArgumentParser(
        prog="PyObfusinator",
        description="Obfuscate python code in weird ways. This is just a fun code golf, not a proper obfuscator",
    )
    parser.add_argument(
        "-i",
        "--input",
        required=False,
        help="Input file. Leave empty to read from stdin",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=False,
        help="Output file. Leave empty to write to stdout",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        required=False,
        action="store_true",
        default=False,
        help="Print extra info",
    )
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument(
        "-f",
        "--inflate",
        action="store_true",
        help="Make the code inflated by using only exec, eval, str, and all",
    )
    action.add_argument(
        "-c",
        "--compress",
        action="store_true",
        help="Compress the code with unicode magic",
    )
    args = parser.parse_args()

    in_file = open(args.input) if args.input else sys.stdin
    out_file = open(args.output, "w") if args.output else sys.stdout
    verbose = args.verbose and args.output  # only be verbose if not writing to stdout

    def vprint(*a, **kw):
        if verbose:
            print(*a, **kw)

    try:
        vprint(f"Reading code from {args.input if args.input else 'stdin'}")
        input_code = in_file.read()

        vprint("Processing")
        if args.inflate:
            output_code = inflate(input_code)
        else:
            output_code = unicode_compress(input_code)

        vprint(f"Writing output to {args.output}")
        if isinstance(output_code, str):
            out_file.write(output_code)
        else:
            out_file.buffer.write(output_code)
        out_file.flush()

        if verbose:
            print_stat(input_code, output_code)

    finally:
        in_file.close()
        out_file.close()


def print_stat(input_code: str, output_code: str | bytes):
    input_char_len = len(input_code)
    input_byte_len = len(input_code.encode("utf-8"))

    if isinstance(output_code, str):
        output_char_len = len(output_code)
        output_byte_len = len(output_code.encode("utf-8"))
    else:
        output_byte_len = len(output_code)
        output_char_len = 92

    print_percentage(input_char_len, output_char_len, "display character")
    print_percentage(input_byte_len, output_byte_len, "byte")


def print_percentage(before: int, after: int, unit: str):
    print(f"Original code length  : {before} ({unit})")
    print(f"Obfuscated code length: {after} ({unit})")
    if after > before:
        print(f"Increased             : {round(after / before * 100 - 100, 2)}%")
    else:
        print(f"Decreased             : {round(100 - after / before * 100, 2)}%")


if __name__ == "__main__":
    main()
