# pytube_patch.py

import re
from pytube.cipher import get_throttling_function_name as original_get_throttling_function_name
from pytube.exceptions import RegexMatchError

def patched_get_throttling_function_name(js: str) -> str:
    """Extract the name of the function that computes the throttling parameter.

    :param str js:
        The contents of the base.js asset file.
    :rtype: str
    :returns:
        The name of the function used to compute the throttling parameter.
    """
    function_patterns = [
        r'\b[a-zA-Z]{1,5}\s*&&\s*[a-zA-Z]{1,5}\.set\(\s*([a-zA-Z]{1,5})\(',  # new pattern
        r'\b[a-zA-Z]{1,5}\s*&&\s*[a-zA-Z]{1,5}\.get\(\s*([a-zA-Z]{1,5})\(',  # new pattern
        r'function\(\w+\)\{var \w+=\w+\.split\(""\),\w+=\[\w+\]\}\(\w+\)',
        r'function(?:\s+[a-zA-Z_$][a-zA-Z_$0-9]*)?\(\)\{[a-zA-Z_$][a-zA-Z_$0-9]*\.\[a-zA-Z_$][a-zA-Z_$0-9]*\(\w+\)\}',
        r'function(?:\s+[a-zA-Z_$][a-zA-Z_$0-9]*)?\(\)\{[a-zA-Z_$][a-zA-Z_$0-9]*\.\[a-zA-Z_$][a-zA-Z_$0-9]*\(\w+',
    ]

    for pattern in function_patterns:
        match = re.search(pattern, js)
        if match:
            return match.group(1)

    raise RegexMatchError(
        caller="get_throttling_function_name",
        pattern="multiple",
    )

def patch_pytube():
    from pytube import cipher
    cipher.get_throttling_function_name = patched_get_throttling_function_name