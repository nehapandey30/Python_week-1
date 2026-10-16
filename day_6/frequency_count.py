"""frequency_count.py

Count word frequencies from a string; handle punctuation and case.
"""

import re


def frequency_count(text: str) -> dict:
    """Return a mapping of word -> count for the given text.

    Words are extracted case-insensitively using a simple word regex.
    """
    words = re.findall(r"\b\w+\b", text.lower())
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq


if __name__ == "__main__":
    fruits = "apple banana sev apple mirchi jackfruit"
    d = frequency_count(fruits)

    # Print the frequency mapping and readable lists of keys/values
    print(d)
    print(list(d.keys()))
    print(list(d.values()))
