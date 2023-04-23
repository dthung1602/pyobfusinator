UNKNOWN_CHAR_MAP = {
    0: "Null (\\0)",
    1: "SOH",
    2: "STX",
    3: "ETX",
    4: "EOT",
    5: "ENQ",
    6: "ACK",
    7: "BEL",
    8: "Backspace (\\b)",
    9: "Tab (\\t) (Did you mean to indent with spaces?)",
    11: "Vertical Tab (\\v)",
    12: "Form Feed (\\f)",
    14: "SO",
    15: "SI",
    16: "DLE",
    17: "DC1",
    18: "DC2",
    19: "DC3",
    20: "DC4",
    21: "NAK",
    22: "SYN",
    23: "ETB",
    24: "CAN",
    25: "EM",
    26: "SUB",
    27: "ESC",
    28: "FS",
    29: "GS",
    30: "RS",
    31: "US",
    127: "DEL",
}


class UnknownCharacterException(ValueError):
    def __init__(self, character: int, line: int) -> None:
        if character < 128:
            descriptor = (
                UNKNOWN_CHAR_MAP[character]
                if character in UNKNOWN_CHAR_MAP
                else f"ASCII {character}"
            )
            super().__init__(f"Line {line}: Cannot encode {descriptor} character.")
        else:
            super().__init__(
                f"Line {line}: Attempt to encode UTF8 character sequence. "
                f"Pyobfusinator only can encode ascii non-control characters and newlines"
            )
