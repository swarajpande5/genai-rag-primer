import re


def split_text(text: str):
    split_text = re.split('\n\n', text)
    return [d for d in split_text if d != ""]
