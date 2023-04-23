from string import printable

from .exception import UnknownCharacterException

__all__ = [
    "inflate",
    "deflate"
]


def inflate(input_code: str) -> str:
    if '"""' in input_code:
        raise ValueError("pyobfusinator doesn't support \"\"\" yet, use ''' instead")

    output_code = generate_boilerplate()

    char_expressions = []
    line = 0
    for c in input_code:
        if c == "\n":
            line += 1
        try:
            char_expressions.append(char_to_expr(c))
        except ValueError:
            raise UnknownCharacterException(ord(c), line)

    output_code += f"exec({'+'.join(char_expressions)})\n"

    output_code = replace_number(output_code)

    return output_code


def deflate(output_code: str) -> str:
    output_code = un_replace_number(output_code)

    boilerplate = generate_boilerplate() + "exec("
    if not (output_code.startswith(boilerplate) and output_code.endswith(")\n")):
        raise ValueError("This code was not obfuscated by pyobfusinator. Cannot deflate.")
    output_code = output_code[len(boilerplate):-2]

    expressions = split_expression(output_code)
    chars = [expr_to_char(e) for e in expressions]

    return "".join(chars)


def split_expression(s: str) -> list[str]:
    stack = 0
    result = []
    begin_exp_idx = 0

    for idx, c in enumerate(s):
        if c == "+":
            if stack == 0:
                result.append(s[begin_exp_idx:idx])
                begin_exp_idx = idx + 1
        elif c == "(":
            stack += 1
        elif c == ")":
            stack -= 1

    result.append(s[begin_exp_idx:])
    return result


SHORT_MAPPING = {
    'l': 'str(str)[2]', 'o': 'str(eval)[16]', 'c': 'str(str)[1]', 'a': 'str(str)[3]',
    's': 'str(str)[4]', 'i': 'str(eval)[3]', 'e': 'str(eval)[19]', 'b': 'str(eval)[1]',
    't': 'str(eval)[5]', 'f': 'str(eval)[10]', 'n': 'str(eval)[8]', 'r': 'str(str)[10]',
    '(': 'str(())[0]', ')': 'str(())[1]', ' ': 'str(str)[6]', '[': 'str([])[0]', ']': 'str([])[1]'
}

REVERSE_SHORT_MAPPING = {v: k for k, v in SHORT_MAPPING.items()}


def generate_boilerplate():
    """
    Execute `from string import printable as b`
    The SHORT_MAPPING provides almost every letter we need for the above import string, except for letter m p g
    These characters can be extracted from str(locals())
    """

    return "exec(str(eval)[10]+str(str)[10]+str(eval)[16]+str(eval(str(str)[2]+str(eval)[16]+str(str)[1]+str(str)[" \
           "3]+str(str)[2]+str(str)[4]+str(())[0]+str(())[1]))[6]+str(str)[6]+str(str)[4]+str(eval)[5]+str(str)[" \
           "10]+str(eval)[3]+str(eval)[8]+str(eval(str(str)[2]+str(eval)[16]+str(str)[1]+str(str)[3]+str(str)[2]+str(" \
           "str)[4]+str(())[0]+str(())[1]))[50]+str(str)[6]+str(eval)[3]+str(eval(str(str)[2]+str(eval)[16]+str(str)[" \
           "1]+str(str)[3]+str(str)[2]+str(str)[4]+str(())[0]+str(())[1]))[6]+str(eval(str(str)[2]+str(eval)[16]+str(" \
           "str)[1]+str(str)[3]+str(str)[2]+str(str)[4]+str(())[0]+str(())[1]))[45]+str(eval)[16]+str(str)[10]+str(" \
           "eval)[5]+str(str)[6]+str(eval(str(str)[2]+str(eval)[16]+str(str)[1]+str(str)[3]+str(str)[2]+str(str)[" \
           "4]+str(())[0]+str(())[1]))[45]+str(str)[10]+str(eval)[3]+str(eval)[8]+str(eval)[5]+str(str)[3]+str(eval)[" \
           "1]+str(str)[2]+str(eval)[19]+str(str)[6]+str(str)[3]+str(str)[4]+str(str)[6]+str(eval)[1])\n"


CHAR_FORMAT_PREFIX = "eval(str(eval)[1]+str([])[0]+str("
CHAR_FORMAT_SUFFIX = ")+str([])[1])"


def char_to_expr(ch: str) -> str:
    if ch in SHORT_MAPPING:
        return SHORT_MAPPING[ch]
    idx = printable.index(ch)
    if idx == -1:
        raise ValueError
    return f"{CHAR_FORMAT_PREFIX}{idx}{CHAR_FORMAT_SUFFIX}"


def expr_to_char(expression: str) -> str:
    if expression in REVERSE_SHORT_MAPPING:
        return REVERSE_SHORT_MAPPING[expression]

    try:
        if not (expression.startswith(CHAR_FORMAT_PREFIX) and expression.endswith(CHAR_FORMAT_SUFFIX)):
            raise
        idx = expression.removeprefix(CHAR_FORMAT_PREFIX).removesuffix(CHAR_FORMAT_SUFFIX)
        return printable[int(idx)]
    except Exception:
        raise ValueError(f"Cannot decompile expression '{expression}'")


def replace_number(code: str):
    for n in reversed(range(len(printable))):
        code = code.replace(str(n), convert_num(n))
    return code


def un_replace_number(code: str):
    for n in reversed(range(len(printable))):
        code = code.replace(convert_num(n), str(n))
    return code


def convert_num(n: int):
    if n == 0:
        return "all([[]])"
    return "+".join(["all([])"] * n)
