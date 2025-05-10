# 🔍 ComfyUI Wildcard YAML Tools
> ✅ Dual-language: [🇷🇺 Русский](#-на-русском) | [🇬🇧 English](#-in-english)
---
## 📌 На русском
Набор утилит для поиска и автоочистки **некорректных символов в YAML wildcard-файлах**, используемых в [ComfyUI Impact Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack) и других нодах.
### 🧰 Что входит
- `wildcard_validator.py`  
  ➤ Проверяет wildcard `.yaml` и `.txt` файлы на:
  - запрещённые символы (например, `0x80`, `0xA9`, `0xE2`, `0xAD`)
  - скрытые байты (включая BOM)
  - плохие UTF-8 символы
- `wildcard_auto_cleaner.py`  
  ➤ Удаляет наиболее распространённые проблемные байты (`C3`, `80`, `A9`).
- `wildcard_auto_cleaner_v2.py`  
  ➤ Расширенная версия, чистит больше символов и перезапускает проверку.
- `wildcard_auto_cleaner_v3.py`  
  ➤ Строгая фильтрация: оставляет **только ASCII-символы**.
---
### 🚀 Использование

1. Помести `.py` файлы в любую рабочую папку.
2. Проверка:
   ```bash
   python wildcard_validator.py
3. Очистка:
```bash
python wildcard_auto_cleaner_v3.py
```
```bash
python wildcard_validator.py
```

📁 Где хранятся wildcard-файлы?
Обычно здесь:
ComfyUI/custom_nodes/ComfyUI-Impact-Pack/wildcards/

❓ Зачем это нужно
Некоторые .yaml wildcard-файлы содержат невидимые или запрещённые символы, из-за которых ComfyUI не может их прочитать. Это вызывает ошибки генерации или сбои.
Скрипты удаляют такие символы автоматически.

🔐 Внимание
Перед запуском утилит обязательно сделай резервную копию файлов wildcards/.

🙋 Автор
Создано совместно с ChatGPT на основе практического опыта.

📄 Лицензия
MIT License
-----------------------------------------------------------------------------------------------------------------------------------------------------------
##🇬🇧 In English
A set of tools for scanning and cleaning wildcard YAML files used in ComfyUI Impact Pack and related extensions.

🧰 Included
wildcard_validator.py
➤ Scans .yaml / .txt wildcard files for:

invisible/forbidden symbols (e.g. 0x80, 0xA9, 0xE2, 0xAD)

BOM markers (EF BB BF)

corrupted or invalid UTF-8

wildcard_auto_cleaner.py
➤ Basic cleaner, removes common corrupted bytes.

wildcard_auto_cleaner_v2.py
➤ Improved cleaner with extended byte filters and rechecks.

wildcard_auto_cleaner_v3.py
➤ Strict mode: removes everything non-ASCII.

🚀 Usage
Place .py scripts into your ComfyUI or working folder.
ComfyUI/custom_nodes/ComfyUI-Impact-Pack/wildcards/

Validate:
 ```bash
python wildcard_validator.py
```
Clean:
 ```bash
python wildcard_auto_cleaner_v3.py
```
Re-validate:
```bash
python wildcard_validator.py
```

📁 Wildcard Files Location
Default path:
ComfyUI/custom_nodes/ComfyUI-Impact-Pack/wildcards/

⚠️ Why This Tool Exists
Some YAML wildcards contain invisible or non-UTF8 characters, which break ComfyUI parsing and prompt generation.
These scripts find and remove them automatically.

📌 Warning
Always back up your wildcard folder before cleaning.

🙋 Author
Created in collaboration with ChatGPT, tested across dozens of Impact Pack setups.

📄 License MIT
