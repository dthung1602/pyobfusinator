import sys
import warnings

from .compress import unicode_compress, unicode_decompress
from .exception import UnknownCharacterException
from .inflate import inflate, deflate

if sys.version_info[0] != 3 or sys.version_info[1] < 10:
    warnings.warn(
        "The python interpreter may break on versions earlier than 3.10", stacklevel=2
    )
