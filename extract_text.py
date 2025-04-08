import re

def extract_string_literals(code):
    """Ambil semua string literal dari kode Python (pakai regex)."""
    pattern = r'(?P<quote>["\'])(?P<text>.*?)(?P=quote)'
    return re.findall(pattern, code)

def replace_string_literals(code, translations):
    """Gantikan string literal dalam kode dengan hasil terjemahan."""
    pattern = r'(["\'])(.*?)(\1)'
    result = ""
    index = 0

    def replacer(match):
        nonlocal index
        quote = match.group(1)
        original = match.group(2)
        translated = translations[index]
        index += 1
        return f'{quote}{translated}{quote}'

    return re.sub(pattern, replacer, code)
