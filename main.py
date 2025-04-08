import os
from extract_text import extract_string_literals, replace_string_literals
from translate import translate_strings

INPUT_FILE = "input/coba.py"
OUTPUT_FILE = "output/translated_example.py"

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        code = f.read()

    string_literals = [text for _, text in extract_string_literals(code)]

    translations = translate_strings(string_literals)

    translated_code = replace_string_literals(code, translations)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(translated_code)

    print(f"✅ Hasil disimpan di: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
