# -*- coding: utf-8 -*-
import os

wildcards_path = r"D:\AI\STMatrix\Packages\ComfyUI\custom_nodes\ComfyUI-Impact-Pack\wildcards"

# Расширенный список нежелательных байтов
BAD_BYTES = [b'\xef', b'\xbb', b'\xbf', b'\xc3', b'\x80', b'\xad', b'\xa9']

def clean_file(file_path):
    with open(file_path, 'rb') as f:
        raw = f.read()

    cleaned = bytearray()
    removed = []

    for i, byte in enumerate(raw):
        b = bytes([byte])
        if b in BAD_BYTES:
            removed.append((i, b))
        else:
            cleaned.append(byte)

    if removed:
        with open(file_path, 'wb') as f:
            f.write(cleaned)
        print(f"🧹 Очищен: {file_path}")
        for pos, b in removed:
            print(f"   ├─ Удалено: позиция {pos}, байт {b.hex().upper()}")
    else:
        print(f"✅ Чисто: {file_path}")

def scan_and_clean(path):
    print("🚀 Глубокая автоочистка YAML-файлов...\n")
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".yaml") or file.endswith(".yml"):
                clean_file(os.path.join(root, file))
    print("\n✅ Обработка завершена.")

if __name__ == "__main__":
    scan_and_clean(wildcards_path)
