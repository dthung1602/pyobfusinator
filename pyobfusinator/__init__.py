import sys

if sys.version_info[0] != 3 or sys.version_info[1] < 10:
    import warnings

    warnings.warn(
        "The python interpreter may break on versions earlier than 3.10",
        stacklevel=2
    )

from .compress import unicode_compress, unicode_decompress
from .exception import UnknownCharacterException
from .inflate import inflate, deflate
