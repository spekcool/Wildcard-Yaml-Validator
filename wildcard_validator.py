# -*- coding: utf-8 -*-
import os
import yaml

wildcards_path = r"D:\AI\STMatrix\Packages\ComfyUI\custom_nodes\ComfyUI-Impact-Pack\wildcards"

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
            print(f"🚫 Проблемный символ в файле: {file_path}")
            print(f"   ├─ Строка: {idx}")
            print(f"   ├─ Позиция: {pos}")
            print(f"   └─ HEX: 0x{byte_val:02X}")
            print("   ➤ Вероятная проблема: Невидимый или запрещённый символ\n")
            return

def is_valid_yaml(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            yaml.load(f, Loader=yaml.FullLoader)
        return True
    except Exception as e:
        print(f"[!] ❌ Ошибка YAML парсинга в {file_path}: {e}")
        return False

def scan_wildcards(path):
    print("🔍 Запуск глубокой проверки YAML-файлов...\n")
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".yaml") or file.endswith(".yml"):
                full_path = os.path.join(root, file)
                pos, bad_byte = scan_for_invalid_chars(full_path)
                if bad_byte is not None:
                    report_invalid_byte(full_path, pos, bad_byte)
                elif not is_valid_yaml(full_path):
                    print(f"🚫 Некорректный YAML: {full_path}")
    print("✅ Проверка завершена.\n")

if __name__ == "__main__":
    scan_wildcards(wildcards_path)
