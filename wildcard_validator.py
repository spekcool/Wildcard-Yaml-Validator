# -*- coding: utf-8 -*-
import os
import yaml

# Automatically use the folder from which the script is launched
wildcards_path = os.getcwd()

def scan_for_invalid_chars(file_path):
    with open(file_path, 'rb') as f:
        raw = f.read()
        for i, byte in enumerate(raw):
            if byte < 0x09 or (0x0E <= byte <= 0x1F) or byte == 0x7F or byte >= 0x80:
                return i, byte
    return None, None

def report_invalid_byte(file_path, pos, byte_val):
    with open(file_path, 'rb') as f:
        lines = f.readlines()
    char_count = 0
    for idx, line in enumerate(lines, start=1):
        char_count += len(line)
        if char_count >= pos:
            print(f"🚫 Invalid character found in file: {file_path}")
            print(f"   ├─ Line: {idx}")
            print(f"   ├─ Position: {pos}")
            print(f"   └─ HEX: 0x{byte_val:02X}")
            print("   ➤ Possible issue: Invisible or forbidden character\n")
            return

def is_valid_yaml(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            yaml.load(f, Loader=yaml.FullLoader)
        return True
    except Exception as e:
        print(f"[!] ❌ YAML parsing error in {file_path}: {e}")
        return False

def scan_wildcards(path):
    print("🔍 Starting deep YAML wildcard validation...\n")
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith((".yaml", ".yml")):
                full_path = os.path.join(root, file)
                pos, bad_byte = scan_for_invalid_chars(full_path)
                if bad_byte is not None:
                    report_invalid_byte(full_path, pos, bad_byte)
                elif not is_valid_yaml(full_path):
                    print(f"🚫 Invalid YAML syntax: {full_path}")
    print("✅ Validation complete.\n")

if __name__ == "__main__":
    scan_wildcards(wildcards_path)
