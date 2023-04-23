# PyObfusinator

Another Python obfuscator, written as a code golf

## Feature

PyObfusinator has 2 methods to obfuscate code:

### Inflation

Rewrite the whole program using only 4 built-in functions: `exec`, `eval`, `str`, `all`, with `()`, `[]`, and `+`

For example, a simple `print('hello world')` becomes

```python
exec(str(eval)[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(str)[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(eval)[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(eval(str(str)[all([])+all([])]+str(eval)[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(str)[all([])]+str(str)[all([])+all([])+all([])]+str(str)[all([])+all([])]+str(str)[all([])+all([])+all([])+all([])]+str(())[all([[]])]+str(())[all([])]))[all([])+all([])+all([])+all([])+all([])+all([])]+str(str)[all([])+all([])+all([])+all([])+all([])+all([])]+str(str)[all([])+all([])+all([])+all([])]+str(eval)[all([])+all([])+all([])+all([])+all([])]+str(str)[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(eval)[all([])+all([])+all([])]+str(eval)[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(eval(str(str)[all([])+all([])]+str(eval)[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(str)[all([])]+str(str)[all([])+all([])+all([])]+str(str)[all([])+all([])]+str(str)[all([])+all([])+all([])+all([])]+str(())[all([[]])]+str(())[all([])]))[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(str)[all([])+all([])+all([])+all([])+all([])+all([])]+str(eval)[all([])+all([])+all([])]+str(eval(str(str)[all([])+all([])]+str(eval)[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(str)[all([])]+str(str)[all([])+all([])+all([])]+str(str)[all([])+all([])]+str(str)[all([])+all([])+all([])+all([])]+str(())[all([[]])]+str(())[all([])]))[all([])+all([])+all([])+all([])+all([])+all([])]+str(eval(str(str)[all([])+all([])]+str(eval)[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(str)[all([])]+str(str)[all([])+all([])+all([])]+str(str)[all([])+all([])]+str(str)[all([])+all([])+all([])+all([])]+str(())[all([[]])]+str(())[all([])]))[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(eval)[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(str)[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(eval)[all([])+all([])+all([])+all([])+all([])]+str(str)[all([])+all([])+all([])+all([])+all([])+all([])]+str(eval(str(str)[all([])+all([])]+str(eval)[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(str)[all([])]+str(str)[all([])+all([])+all([])]+str(str)[all([])+all([])]+str(str)[all([])+all([])+all([])+all([])]+str(())[all([[]])]+str(())[all([])]))[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(str)[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(eval)[all([])+all([])+all([])]+str(eval)[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(eval)[all([])+all([])+all([])+all([])+all([])]+str(str)[all([])+all([])+all([])]+str(eval)[all([])]+str(str)[all([])+all([])]+str(eval)[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(str)[all([])+all([])+all([])+all([])+all([])+all([])]+str(str)[all([])+all([])+all([])]+str(str)[all([])+all([])+all([])+all([])]+str(str)[all([])+all([])+all([])+all([])+all([])+all([])]+str(eval)[all([])])
exec(eval(str(eval)[all([])]+str([])[all([[]])]+str(all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([]))+str([])[all([])])+str(str)[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(eval)[all([])+all([])+all([])]+str(eval)[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(eval)[all([])+all([])+all([])+all([])+all([])]+str(())[all([[]])]+eval(str(eval)[all([])]+str([])[all([[]])]+str(all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([]))+str([])[all([])])+eval(str(eval)[all([])]+str([])[all([[]])]+str(all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([]))+str([])[all([])])+str(eval)[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(str)[all([])+all([])]+str(str)[all([])+all([])]+str(eval)[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(str)[all([])+all([])+all([])+all([])+all([])+all([])]+eval(str(eval)[all([])]+str([])[all([[]])]+str(all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([]))+str([])[all([])])+str(eval)[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(str)[all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])]+str(str)[all([])+all([])]+eval(str(eval)[all([])]+str([])[all([[]])]+str(all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([]))+str([])[all([])])+eval(str(eval)[all([])]+str([])[all([[]])]+str(all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([]))+str([])[all([])])+str(())[all([])]+eval(str(eval)[all([])]+str([])[all([[]])]+str(all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([])+all([]))+str([])[all([])]))
```

### Unicode magic

"Compress" the whole program using zalgo text

For example, `print('hello world')` becomes

```python
b='E͉͎͔͈͐͒̈̇͌͌ͅ͏̀͗͏͒͌̈́̇̉ͯ'.encode();exec(''.join(chr(((h<<6&64|c&63)+22)%133+10)for h,c in zip(b[1::2],b[2::2])))
```

## Installation

1. Clone this project
2. Make sure you have [poetry](https://python-poetry.org/) installed
3. Run
    ```shell
    poetry install
    ```

## Command line

Once installed, call the command line directly

```pyobfusinator -i source.py -o dest.py -f```

Or using the python module

```python3 -m pyobfusinator -i source.py -o dest.py -f```

All available options:

```text
pyobfusinator [-h] [-i INPUT] [-o OUTPUT] [-v] (-f | -c)
options:
  -h, --help                  Show this help message and exit
  -i INPUT, --input INPUT     Input file. Leave empty to read from stdin
  -o OUTPUT, --output OUTPUT  Output file. Leave empty to write to stdout
  -v, --verbose               Print extra info
  -f, --inflate               Make the code inflated by using only exec, eval, str, and all
  -c, --compress              Compress the code with unicode magic
```

## API

```python
from pyobfusinator import inflate, deflate, unicode_compress, unicode_decompress

text = "print('hello world')"

# inflate obfuscation
inflated_text = inflate(text)  # exec(str(eval)[all([])+all([])...
original_text = deflate(inflated_text)  # print('hello world')

# unicode magic obfuscation
compressed_text = unicode_compress(text)  #  b='E͉͎͔͈͐͒̈̇͌͌ͅ͏̀͗͏͒͌̈́̇̉ͯ'.encode()...
original_text = unicode_decompress(compressed_text)  # print('hello world')
```

## How does it work?

### Inflation

Numbers:

```python
0 == all([[]])
1 == all([])  # this equals True
2 == all([]) + all([])
3 == all([]) + all([]) + all([])
...
```

Once we get the numbers down, we can use them to access any index of a string to obtain any character. 

```python
"l" == str(str)[2]    # str(str)  == "<class 'str'>"
"o" == str(eval)[16]  # str(eval) == "<built-in function eval>"
"b" == str(eval)[1]   # str(eval) == "<built-in function eval>"
...
```

This way, we are able to get 17 characters. With this 17 chars, we can write `exec("from string import printable as b")`

Finally, we can represent any printable by evaluating `eval("b[idx]")`

### Unicode zalgo magic

Idea and implementation from [DaCoolOne](https://github.com/DaCoolOne/DumbIdeas/blob/main/reddit_ph_compressor/out.py) reddit comment.
[Link](https://www.reddit.com/r/ProgrammerHumor/comments/yqof9f/comment/ivrd9ur/?utm_source=share&utm_medium=web2x&context=3)

I love it so much that I include it here
