# -*- coding: utf-8 -*-
import os

# 📂 Текущая рабочая директория, где запускается скрипт
wildcards_path = os.getcwd()

def clean_strict_ascii(file_path):
    with open(file_path, 'rb') as f:
        raw = f.read()

    cleaned = bytearray()
    removed = []

    for i, b in enumerate(raw):
        if 32 <= b <= 126 or b in (9, 10, 13):  # Разрешённые: печатные ASCII + \t \n \r
            cleaned.append(b)
        else:
            removed.append((i, b))

    if removed:
        with open(file_path, 'wb') as f:
            f.write(cleaned)
        print(f"🧹 Очищен: {file_path}")
        for pos, b in removed:
            print(f"   ├─ Удалено: позиция {pos}, байт {b:02X}")
    else:
        print(f"✅ Чисто: {file_path}")

def scan(path):
    print("🚀 Строгая очистка только ASCII...\n")
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith((".yaml", ".yml")):
                clean_strict_ascii(os.path.join(root, file))
    print("\n✅ Обработка завершена.")

if __name__ == "__main__":
    scan(wildcards_path)
